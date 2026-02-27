import pytest
from escola import verificador_media as vm

def test_erros():
    with pytest.raises(TypeError, match="Insira um valor numérico"):
        vm("oito")