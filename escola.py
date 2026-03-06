def verificador_media(media:int|float) -> str:
    """Verifica uma média para retornar se o aluno está aprovado, reprovado ou de recuperação."""

    # isistence verifica o tipo de dado
    if not isinstance(media, int|float):
        raise TypeError ("Insira um valor numérico")
    
    elif media >= 7 and media <= 10:
        return "Aprovado(a)"

    elif media <= 5 and media >= 0:
        return "Reprovado(a)"

    elif media > 5 and media < 7:
        return "Recuperação"
    
    else:
        raise ValueError ("O valor deve ser maior ou igual a 0 e menor ou igual a 10")
    

if __name__ == "__main__":
    print(verificador_media("casa"))

# Testes unitários.