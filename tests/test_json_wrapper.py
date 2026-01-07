from poocam_core.interpolator import Interpolator
from poocam_core.json_wrapper import JsonWrapper


def test_wrapper():
    interp = Interpolator(16, 16)
    matrix = [
        [18.1, 21.1, 27.0, 20.2],
        [18.1, 23.3, 29.1, 25.6],
        [17.9, 21.8, 23.5, 23.0],
        [18.5, 20.2, 21.0, 21.0]
    ]
    json_wrapper = JsonWrapper()
    wrapped: str = json_wrapper.wrap(matrix)
    assert wrapped.startswith('{')

