import pytest
from escola import verificador_media as vm

def test_typeerror():
    with pytest.raises(TypeError, match="Insira um valor numérico"):
        vm("casa")

def test_value_menor_que_0():
    with pytest.raises(ValueError, match="O valor deve ser maior ou igual a 0 e menor ou igual a 10"):
        vm(-5)

def test_value_maior_que_10():
    with pytest.raises(TypeError, match="O valor deve ser maior ou igual a 0 e menor ou igual a 10"):
        vm(2000)