from enum import Enum


class Sensors(Enum):
    WATER_LEVEL = 'water-level'
    WATER_TEMP = 'water-temp'
    AIR_TEMP = 'air-temp'
    HUMIDITY = 'humidity'
    PH = 'ph'
    LIGHT = 'light'
    TDS = 'tds'
    EC = 'ec'
