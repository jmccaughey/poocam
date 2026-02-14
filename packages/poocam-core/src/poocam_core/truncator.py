import math

class Truncator:
    def __init__(self, places: int) -> None:
        self.places = places

    def truncate_to_places(self, fin: float) -> float:
        multiplier = 10 ** self.places
        return int(fin * multiplier) / multiplier

    def truncate(self, data: list[list[float]]) -> None:
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = self.truncate_to_places(data[i][j])
