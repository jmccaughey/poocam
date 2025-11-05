from abc import ABC, abstractmethod
from typing import List


class SensorDataSource(ABC):
    @abstractmethod
    def read(self) -> List[List[float]]:
        pass
