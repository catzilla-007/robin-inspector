from os import getenv
from enum import Enum


class Config(Enum):
    DB_HOST = 'DB_HOST'
    DB_NAME = 'DB_NAME'


class Environment:
    @staticmethod
    def get(config: Config):
        return getenv(config)
