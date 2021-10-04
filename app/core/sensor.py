from abc import ABC, abstractmethod
from app.sensors import Sensors


class Sensor(ABC):
    TYPE: Sensors

    @abstractmethod
    def collect_value(self):
        pass

    def get_value(self) -> any:
        return self.collect_value()
