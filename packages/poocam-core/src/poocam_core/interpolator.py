from scipy.ndimage import zoom
import numpy as np

class Interpolator:
    def __init__(self, x_zoom: int, y_zoom: int):
        self.x_zoom = x_zoom
        self.y_zoom = y_zoom

    def interpolate(self, data: list[list[float]]) -> list[list[float]]:
        resized_data = zoom(data, [self.x_zoom, self.y_zoom], order=3)
        return resized_data
