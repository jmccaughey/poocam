import math

class Truncator:
    def truncate(self, data: list[list[float]]) -> None:
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = float(math.trunc(data[i][j]))

    def truncate_to_int(self, data: list[list[float]]) -> list[list[int]]:
        result: list[list[int]] = []

        for row in data:
            out_row: list[int] = []
            for x in row:
                out_row.append(math.trunc(x))
            result.append(out_row)

        return result
