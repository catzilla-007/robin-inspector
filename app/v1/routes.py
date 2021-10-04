from fastapi import APIRouter

from app.core.sensor_factory import SensorFactory
from app.sensors import Sensors

PREFIX = '/api/v1'
NOT_FOUND = {'description': 'NOT FOUND'}

router = APIRouter(prefix=PREFIX, tags=['v1'], responses={404: NOT_FOUND})


@router.get('/water-level', tags=['water-level'])
async def get_water_level():
    water_level = SensorFactory.get_sensor(Sensors.WATER_LEVEL)
    return {'value': water_level.get_value()}
