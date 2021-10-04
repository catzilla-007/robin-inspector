from app.core.errors import RobinException
from app.sensors.water_level import *


class SensorFactory(object):
    @staticmethod
    def get_sensor(sensor: Sensors):
        for kls in Sensor.__subclasses__():
            if sensor == kls.TYPE:
                return kls()
        raise RobinException(f'Sensor {sensor} not found!')
