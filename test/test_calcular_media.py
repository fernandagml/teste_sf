from boletim.calculos import calcular_media
import pytest

@pytest.mark.parametrize("notas, resultado",
                         [
                             ([10, 5, 3], 6.0),
                             ([5.5, 6.3, 8.2], 6.7),
                             ([6, 7, 6.7], 6.6),
                             ([8], 8.0),
                             ([1, 10, 8, 4, 9, 9, 8.5], 7.1),
                             ([0, 0, 0], 0.0),
                             ([10, 10, 10], 10.0)
                         ])

def test_boletim_happy_path(notas, resultado):
    assert calcular_media(notas) == resultado