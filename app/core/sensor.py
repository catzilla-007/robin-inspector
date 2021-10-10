from abc import ABC, abstractmethod
from app.sensors import Sensors

from .response import Response


class Sensor(ABC):
    TYPE: Sensors

    @abstractmethod
    def collect_value(self) -> Response:
        pass

    def get_value(self) -> Response:
        return self.collect_value()
