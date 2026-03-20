import pytest
from boletim.calculos import calcular_media as cm

# @pytest.mark.parametrize(
# ("entrada", "saida"),
# [
#     ([8, 10], 9.0),
#     ([5.5, 9.5], 7.5)
# ]
# )

# def test_happy_path(entrada, saida):
#     assert cm(entrada) == saida

print(cm([8, 10]))