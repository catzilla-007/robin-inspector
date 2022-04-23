from fastapi import APIRouter

from .routes import router


PREFIX = '/v1'
NOT_FOUND = {'description': 'NOT FOUND'}

v1 = APIRouter(prefix=PREFIX, tags=['api'], responses={404: NOT_FOUND})

v1.include_router(router)
