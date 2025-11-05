# file: random_sensor.py
import random
from typing import List
from poocam_core.sensor_data_source import SensorDataSource


class RandomSensor(SensorDataSource):
    """
    Fake sensor that returns random numbers (for testing).
    """

    def __init__(self, rows: int, cols: int, min_val: float, max_val: float):
        self.rows = rows
        self.cols = cols
        self.min = min_val
        self.max = max_val

    def read(self) -> List[List[float]]:
        return [
            [random.uniform(self.min, self.max) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
