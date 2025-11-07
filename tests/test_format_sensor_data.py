import socket
import time

from poocam_core.random_sensor import RandomSensor
from poocam_core.sensor_data_source import SensorDataSource
from poocam_core.sensor_data_formatter import SensorDataFormatter
import json
import threading

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

def test_random_sensor_socket():
    sensor: SensorDataSource = RandomSensor(8, 8, 10.0, 35.0, host="127.0.0.1", port=9090)
    socket_thread = threading.Thread(target=sensor.serve, args=())
    socket_thread.start()
    time.sleep(5)
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 9090))
    f = sock.makefile('r', encoding='utf-8')
    try:
        line = f.readline()
        print(f"Received: {line.strip()}")
    finally:
        f.close()
        sock.close()
        sensor.stop_server()
        socket_thread.join()
    parsed = json.loads(line)
    assert len(parsed) == 8
    assert len(parsed[0]) == 8
