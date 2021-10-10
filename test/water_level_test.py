from datetime import datetime

from app.core.response import Response
from app.sensors.water_level import WaterLevel


def test_water_level():
    water_level = WaterLevel()
    expected = Response(
        type=water_level.TYPE,
        value="high",
        timestamp=datetime.now()
    )

    result = water_level.get_value()

    assert result.value == expected.value
    assert result.type == expected.type
