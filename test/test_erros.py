import pytest
from boletim.calculos import calcular_media

def test_str():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media("NOVE")

def test_value_menor_que_0():
    with pytest.raises(ValueError):
        calcular_media([-5, -10, -8])

def test_value_maior_que_10():
    with pytest.raises(ValueError):
        calcular_media([12, 50, 67])

def test_value_str_int():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media([8, "nove", 5])

def test_value_vazio():
    with pytest.raises(ValueError, match="A lista de notas não pode estar vazia"):
        calcular_media([])

def test_value_str_lista():
    with pytest.raises(TypeError, match="A lista de notas não pode estar vazia"):
        calcular_media(["nove", "dez", "dois"])

def test_value_int():
    with pytest.raises(TypeError):
        calcular_media(8)