from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class User:
    token: str


@dataclass
class Config:
    user: User


def load_config():
    config = Config(
        user=User(
            token=os.getenv("TOKEN")
        )
    )
    return config
