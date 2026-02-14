from poocam_core.truncator import Truncator


def test_truncate():
    truncator: Truncator = Truncator(1)
    data: list[list[float]] = [[2.34343, 5.123123],[8.5876, 14.567563]]
    truncator.truncate(data)
    assert data[0][0] == 2.3
    assert data[1][1] == 14.5

def test_truncate_two():
    truncator: Truncator = Truncator(2)
    data: list[list[float]] = [[2.34343, 5.123123],[8.5876, 14.567563]]
    truncator.truncate(data)
    assert data[0][0] == 2.34
    assert data[1][1] == 14.56
