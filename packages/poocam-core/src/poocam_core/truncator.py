import math

class Truncator:
    def truncate(self, data: list[list[float]]) -> None:
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = float(math.trunc(data[i][j]))
