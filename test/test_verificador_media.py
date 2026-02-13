import pytest
from escola import verificador_media as vm

def test_verificar_aprovado():
    assert vm(8) == "Aprovado(a)"