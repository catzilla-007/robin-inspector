from enum import Enum

from app.core.sensor import Sensor
from . import Sensors


class WaterLevels(Enum):
    NORMAL = 'normal'
    LOW = 'low'
    HIGH = 'high'


class WaterLevel(Sensor):
    TYPE = Sensors.WATER_LEVEL

    def collect_value(self) -> WaterLevels:
        return WaterLevels.HIGH
