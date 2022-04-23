from fastapi import FastAPI
from app.api import api

from app.db.database import Database

Database.connect()
server = FastAPI()

server.include_router(api)
