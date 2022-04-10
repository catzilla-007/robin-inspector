from mongoengine import connect, disconnect
from app.config.config import ConfigNames, Config


class Database:
    @staticmethod
    def connect():
        try:
            print('connecting to database')
            db = Config.get(ConfigNames.DB_NAME.value)
            host = Config.get(ConfigNames.DB_HOST.value)
            connect(db, host=host)
            print('connected')
        except Exception as e:
            print(f'failed to connect to database {e}')

    def __del__(self):
        try:
            print('disconnecting to database...')
            disconnect('going-sunny')
        except Exception as e:
            print(f'failed to disconnect to database {e}')
