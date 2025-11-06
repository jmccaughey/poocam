from poocam_core.random_sensor import RandomSensor
from poocam_core.sensor_data_source import SensorDataSource
from poocam_core.sensor_data_formatter import SensorDataFormatter
import json

def test_matrix_to_json_returns_valid_json():
    matrix = [
        [1.19, 2.1, 3.0],
        [4.9, 5.39, 6.9]
    ]
    formatter: SensorDataFormatter = SensorDataFormatter()
    result = formatter.format_sensor_data(matrix)
    parsed = json.loads(result)
    assert parsed == matrix

def test_random_sensor():
    sensor: SensorDataSource = RandomSensor(8, 8, 10.0, 35.0)
    formatter: SensorDataFormatter = SensorDataFormatter()
    red_data = sensor.read()
    result = formatter.format_sensor_data(red_data)
    parsed = json.loads(result)
    assert parsed == red_data