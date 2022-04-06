from mongoengine import connect, disconnect
from app.env.environment import Config, Environment


class Database:
    @staticmethod
    def connect():
        try:
            print('connecting to database')
            db = Environment.get(Config.DB_NAME.value)
            host = Environment.get(Config.DB_HOST.value)
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
