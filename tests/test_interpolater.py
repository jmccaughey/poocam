from poocam_core.interpolator import Interpolator

def test_zoom():
    interp = Interpolator(16, 16)
    matrix = [
        [18.1, 21.1, 27.0, 20.2],
        [18.1, 23.3, 29.1, 25.6],
        [17.9, 21.8, 23.5, 23.0],
        [18.5, 20.2, 21.0, 21.0]
    ]
    new_data = interp.interpolate(matrix)
    assert 64 == len(new_data)
    assert 64 == len(new_data[0])
