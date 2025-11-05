import time
from typing import List
from poocam_core.sensor_data_source import SensorDataSource

import board
import busio
import adafruit_amg88xx


class GridEyeSensor(SensorDataSource):
    def __init__(self):
        self.i2c_bus = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_amg88xx.AMG88XX(self.i2c_bus)
        # let the sensor initialize
        time.sleep(0.1)

    def read(self) -> List[List[float]]:
        return self.sensor.pixels
