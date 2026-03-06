def verificador_media(media:int|float) -> str:
    """Verifica uma média para retornar se o aluno está aprovado, reprovado ou de recuperação."""

    if media >= 7 and media <= 10:
        return "Aprovado(a)"

    elif media <= 5 and media >= 0:
        return "Reprovado(a)"

    elif media > 5 and media < 7:
        return "Recuperação"

if __name__ == "__main__":
    print(verificador_media("casa"))

# Testes unitários.