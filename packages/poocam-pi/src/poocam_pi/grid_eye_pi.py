import time
from poocam_core.sensor_data_source import SensorDataSource

import board
import busio
import adafruit_amg88xx


class GridEyeSensor(SensorDataSource):
    def __init__(self, host: str = "0.0.0.0", port: int = 9090, zoom: int = 1):
        super().__init__(host=host, port=port, zoom=zoom)
        self.i2c_bus = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_amg88xx.AMG88XX(self.i2c_bus)
        # let the sensor initialize
        time.sleep(0.1)

    def read(self) -> list[list[float]]:
        return self.sensor.pixels
