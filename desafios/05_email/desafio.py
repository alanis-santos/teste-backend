def email_valido(email: str) -> bool:
    """
    Verifica se um e-mail "parece" correto, sem regex.

    Regras:
        - Não pode conter espaços
        - Deve ter exatamente um caractere '@'
        - Deve ter pelo menos um ponto '.'

    Retorna True se válido, False caso contrário.
    """
    return " " not in email and email.count("@") == 1 and "." in email