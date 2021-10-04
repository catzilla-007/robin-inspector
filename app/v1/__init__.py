from fastapi import APIRouter

from app.sensors.water_level import WaterLevel

PREFIX = '/api/v1'
NOT_FOUND = {'description': 'NOT FOUND'}

router = APIRouter(prefix=PREFIX, tags=['v1'], responses={404: NOT_FOUND})


@router.get('/water-level', tags=['water-level'])
async def get_water_level():
    water = WaterLevel()
    return {'water': await water.get_water_level()}
