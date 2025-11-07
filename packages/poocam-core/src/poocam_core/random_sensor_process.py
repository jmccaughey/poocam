import socket

from poocam_core.random_sensor import RandomSensor
from poocam_core.sensor_data_source import SensorDataSource

def start_server():
    sensor_data_source: SensorDataSource = RandomSensor(8, 8, 10.0, 35.0, host="127.0.0.1", port=9090)
    sensor_data_source.serve()

if __name__ == "__main__":
    start_server()