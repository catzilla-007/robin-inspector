from fastapi import APIRouter

from app.core.sensor_factory import SensorFactory
from app.core.response import Response
from app.sensors import Sensors


PREFIX = '/api/v1'
NOT_FOUND = {'description': 'NOT FOUND'}

router = APIRouter(prefix=PREFIX, tags=['v1'], responses={404: NOT_FOUND})


@router.get('/water-level', tags=['water-level', 'sensor'], response_model=Response)
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


@router.get('/arduinos', tags=['arduino'])
async def get_arduinos():
    return [
      {
        "id": "uuid",
        "name": "franky-1",
        "state": "active",
        "connection": "connected",
        "startedOn": "time",
        "stoppedOn": None,
        "ip": "192.168.1.3",
        "port": 80
      },
      {
        "id": "uuid",
        "name": "franky-2",
        "state": "inactive",
        "connection": "disconnected",
        "startedOn": None,
        "stoppedOn": None,
        "ip": "192.168.1.2",
        "port": 80
      }
    ]


@router.get('/arduinos/<uuid>', tags=['arduino'])
async def get_arduino():
    return {
      "id": "uuid",
      "name": "franky-3",
      "state": "active",
      "connection": "reachable",
      "startedOn": "time",
      "stoppedOn": None,
      "ip": "192.168.1.4",
      "port": 80
    }


@router.post('/arduinos', tags=['arduino'])
async def create_arduino():
    return {
        'arduino': 1,
    }

