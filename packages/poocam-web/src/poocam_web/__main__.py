# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import asyncio
import os
import io
import sys
import socket
import json

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import uvicorn

from poocam_core.random_sensor import RandomSensor
from poocam_core.interpolator import Interpolator
from poocam_core.sensor_data_formatter import SensorDataFormatter
from poocam_core.sensor_data_source import SensorDataSource
from poocam_core.truncator import Truncator

# from poocam_pi.grid_eye_pi import GridEyeSensor

sensor: SensorDataSource = RandomSensor(8, 8, 12.0, 30.0)
# sensor: SensorDataSource = GridEyeSensor()
inerpolator: Interpolator = Interpolator(8, 8)
truncator: Truncator = Truncator()

app = FastAPI()
print(f"current dir: {os.getcwd()} args: {sys.argv}")
sensor_data_formatter = SensorDataFormatter()

static_base: str = ""
host: str = "127.0.0.1"
port: int = 9090
if (len(sys.argv) > 1):
    static_base = sys.argv[1]

if (len(sys.argv) > 2):
    host = sys.argv[2]

if (len(sys.argv) > 3):
    port = int(sys.argv[3])

app.mount("/static", StaticFiles(directory=f"{static_base}static"), name="static")

@app.websocket("/ws/ir")
async def websocket_ir(websocket: WebSocket):
    print("waiting for connection...")
    await websocket.accept()
    print("...got connection")
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"connecting to host {host}:{port}")
        sock.connect((host, port))
        f = sock.makefile('r', encoding='utf-8')
        while True:
            sensor_line: str = f.readline()
            sensor_data: list[list[float]] = json.loads(sensor_line)
            scaled_data: list[list[float]] = inerpolator.interpolate(sensor_data)
            truncator.truncate(scaled_data)
            data = sensor_data_formatter.format_sensor_data(scaled_data)
            await websocket.send_bytes(data)
            await asyncio.sleep(0.1)
    finally:
        sock.close()

if __name__ == "__main__":
    print(f"invoking uvicorn.run...")
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, log_level="info")
