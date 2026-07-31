def padronizar_nomes(nomes: list[str]) -> list[str]:
    """
    Recebe uma lista de nomes "sujos" e retorna os nomes formatados
    em Title Case, sem espaços nas extremidades.
    """
    return [" ".join(nome.split()).title() for nome in nomes]
