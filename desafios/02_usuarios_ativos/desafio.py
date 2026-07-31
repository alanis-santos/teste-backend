def filtrar_usuarios_ativos(usuarios: list[dict]) -> list[str]:
    """
    Recebe uma lista de dicionários no formato {"nome": str, "ativo": bool}.

    Retorna apenas os nomes dos usuários com ativo=True.
    Se nenhum estiver ativo, retorna lista vazia.
    """
    nomes_ativos = []
    for usuario in usuarios:
        if usuario.get("ativo") is True:
            nomes_ativos.append(usuario["nome"])
    return nomes_ativos
