import requests
from github import Github, Auth
from github.GithubException import BadCredentialsException, GithubException
import os
import subprocess

from .config import load_config

config = load_config()


def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout + result.stderr)


def get_current_folder() -> str:
    dir = os.getcwd().split('/')[-1]
    return dir


class NewRepository:

    def __init__(self):
        self.path = get_current_folder()

    @staticmethod
    def get_user():
        try:
            auth = Auth.Token(config.user.token)
            git = Github(auth=auth)
            return git.get_user()
        except BadCredentialsException:
            print('[ERROR] Your token is not correct')
        except requests.exceptions.ConnectionError:
            print('[ERROR] Connection failed')

    def new_repository(self) -> None:
        try:
            user = self.get_user()
            repo = user.create_repo(self.path)
            print(f'[SUCCESS] Repository {repo.name} created')
        except GithubException as e:
            print(f'[ERROR] {e.data.get("message")}')
            print(f'[ERROR] {e.data.get("errors")[0].get("message").capitalize()}')


class ConnectRepository:
    cmd = ['echo "# create-repository-script" >> README.md', 'git init', 'git add README.md',
           'git commit -m "init"',
           f'git remote add origin https://github.com/{NewRepository.get_user().login}/{get_current_folder()}',
           'git push -u origin main']

    @staticmethod
    def search_repository(repo: str) -> bool:
        try:
            repos = [i for i in NewRepository.get_user().get_repos()]
            return repo in repos
        except Exception as e:
            print(f'[ERROR] {e}')

    def connect(self):
        try:
            for i in self.cmd:
                print(i)
                run_command(i)
            print('[SUCCESS] Connected to repository')
        except Exception or GithubException as e:
            print(f'[ERROR] {e}')


