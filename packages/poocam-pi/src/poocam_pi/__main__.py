import socket

from poocam_core.sensor_data_source import SensorDataSource
from poocam_pi.grid_eye_pi import GridEyeSensor

def start_server():
    sensor_data_source: SensorDataSource = GridEyeSensor(zoom=16)
    sensor_data_source.serve()

if __name__ == "__main__":
    start_server()