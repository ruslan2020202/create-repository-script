import subprocess


def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout + result.stderr


cmds = ['foldersize', 'ls', 'foldersize']


def main():
    for i in cmds:
        print(run_command(i))


main()