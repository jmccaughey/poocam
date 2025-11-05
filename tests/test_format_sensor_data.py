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