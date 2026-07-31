def senha_forte(senha: str) -> bool:
    """
    Verifica se uma senha é considerada forte.

    Regras:
        - Pelo menos 8 caracteres
        - Pelo menos uma letra maiúscula
        - Pelo menos uma letra minúscula
        - Pelo menos um número

    Retorna True se forte, False caso contrário.
    """
    if len(senha) < 8:
        return False

    tem_maiuscula = any(caracter.isupper() for caracter in senha)
    tem_minuscula = any(caracter.islower() for caracter in senha)
    tem_numero = any(caracter.isdigit() for caracter in senha)

    return tem_maiuscula and tem_minuscula and tem_numero
