from fastapi import APIRouter

from .v1 import v1


PREFIX = '/api'
NOT_FOUND = {'description': 'NOT FOUND'}

api = APIRouter(prefix=PREFIX, tags=['api'], responses={404: NOT_FOUND})

api.include_router(v1)
