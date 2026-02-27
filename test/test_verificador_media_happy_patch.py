import pytest
from escola import verificador_media as vm

def test_verificar_aprovado():
    assert vm(8) == "Aprovado(a)"

def test_verificar_reprovado():
    assert vm(4) == "Reprovado(a)"

def test_verificar_recuperacao():
    assert vm(6) == "Recuperação"