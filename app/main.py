from fastapi import FastAPI
from app import v1

api = FastAPI()

api.include_router(v1.router)
