import json
from typing import List

class SensorDataFormatter:

    def format_sensor_data(self, sensor_data: List[List[float]]) -> str:
        return json.dumps(sensor_data)
