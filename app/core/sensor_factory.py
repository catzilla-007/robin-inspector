from app.core.errors import RobinException
from app.core.sensor import Sensor
from app.sensors import Sensors

# subclasses
from app.sensors.water_level import WaterLevel


class SensorFactory(object):
    @staticmethod
    def get_sensor(sensor: Sensors):
        # TODO: this can be faster/efficient
        for kls in Sensor.__subclasses__():
            if sensor == kls.TYPE:
                return kls()
        raise RobinException(f'Sensor {sensor} not found!')
