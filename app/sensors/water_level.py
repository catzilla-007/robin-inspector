from enum import Enum

from app.core.sensor import Sensor
from app.core.response import Response
from . import Sensors


class WaterLevels(Enum):
    NORMAL = 'normal'
    LOW = 'low'
    HIGH = 'high'


class WaterLevel(Sensor):
    TYPE = Sensors.WATER_LEVEL

    def collect_value(self) -> Response:
        return Response(
            type=self.TYPE,
            value=WaterLevels.HIGH.value
        )
