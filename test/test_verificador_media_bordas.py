import pytest
from escola import verificador_media as vm

# Teste parametrizado: com uma única função testo vários valores.
@pytest.mark.parametrize(
    ("entrada", "saida"),
    [
        (8, "Aprovado(a)"),
        (4, "Reprovado(a)"),
        (6, "Recuperação"),
        (7, "Aprovado(a)"),
        (5, "Reprovado(a)"),
        (5.5, "Recuperação"),
        (0, "Reprovado(a)"),
        (10, "Aprovado(a)")
    ]
)

def test_bordas(entrada, saida):
    assert vm(entrada) == saida