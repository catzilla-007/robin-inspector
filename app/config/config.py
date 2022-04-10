from os import getenv
from enum import Enum


class ConfigNames(Enum):
    DB_HOST = 'DB_HOST'
    DB_NAME = 'DB_NAME'


class Config:
    @staticmethod
    def get(config: ConfigNames):
        return getenv(config)
