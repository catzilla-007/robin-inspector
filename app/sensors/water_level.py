# might need to have a specific parent class
class WaterLevel(object):
    TYPE = 'water-level'

    async def get_water_level(self):
        # gets water level from gpio and translates it to the desired value
        return 'normal'

    async def change_water_level(self, level: str):
        # for version 2
        # adjusts water level, then a worker will constantly
        # watch until the certain water level is reached
        return level
