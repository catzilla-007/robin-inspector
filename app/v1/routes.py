from fastapi import APIRouter

from app.core.sensor_factory import SensorFactory
from app.core.response import Response
from app.sensors import Sensors


PREFIX = '/api/v1'
NOT_FOUND = {'description': 'NOT FOUND'}

router = APIRouter(prefix=PREFIX, tags=['v1'], responses={404: NOT_FOUND})


@router.get('/water-level', tags=['water-level'], response_model=Response)
async def get_water_level():
    return SensorFactory.get_sensor(Sensors.WATER_LEVEL).get_value()


@router.get('/status')
async def get_status():
    return {
        'totalFrankys': 3,
        'activeFrankys':1,
        'version': '1.0.3',
        'serverStartedOn': 'time',
    }
