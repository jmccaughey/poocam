Find warm things. 

Start FastAPI app that serves thermal data:

```shell
uv run -m poocam_web packages/poocam-web/
```

Open web browser to view (fake) thermal data:

```
open "http://<IP>:8000/static/index.html
```

To view real thermal data from a `grideye` https://www.adafruit.com/product/3538

1. Add dependencies:
```shell
uv add --package poocam-pi adafruit-blinka adafruit-circuitpython-amg88xx rpi-gpio
```
2. Edit `packages/poocam-web/src/poocam_web/__main__.py`
```shell
  [uncomment] `# from poocam_pi.grid_eye_pi import GridEyeSensor`
  [replace RandomSensor] `sensor: SensorDataSource = GridEyeSensor()`
```
