from fastapi import FastAPI
from app import v1

from app.db.database import Database

Database.connect()
api = FastAPI()

api.include_router(v1.router)
