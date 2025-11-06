# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import asyncio
import os
import io
import sys

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import uvicorn

from poocam_core.random_sensor import RandomSensor
from poocam_core.interpolator import Interpolator
from poocam_core.sensor_data_formatter import SensorDataFormatter
from poocam_core.sensor_data_source import SensorDataSource
# from poocam_pi.grid_eye_pi import GridEyeSensor

sensor: SensorDataSource = RandomSensor(8, 8, 12.0, 30.0)
# sensor: SensorDataSource = GridEyeSensor()
inerpolator: Interpolator = Interpolator(8, 8)

app = FastAPI()
print(f"current dir: {os.getcwd()} args: {sys.argv}")
sensor_data_formatter = SensorDataFormatter()

static_base: str = ""
if (len(sys.argv) > 1):
    static_base = sys.argv[1]

app.mount("/static", StaticFiles(directory=f"{static_base}static"), name="static")

@app.websocket("/ws/ir")
async def websocket_ir(websocket: WebSocket):
    print("waiting for connection...")
    await websocket.accept()
    print("...got connection")
    while True:
        sensor_data: list[list[float]] = sensor.read()
        scaled_data: list[list[float]] = inerpolator.interpolate(sensor_data)
        data = sensor_data_formatter.format_sensor_data(scaled_data)
        await websocket.send_bytes(data)
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    print(f"invoking uvicorn.run...")
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, log_level="info")
