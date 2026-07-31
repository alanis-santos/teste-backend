def limpar_csv_numeros(linha: str) -> str:
    """
    Recebe uma linha CSV delimitada por ';' e retorna a mesma linha
    com as vírgulas dos números convertidas em pontos.

    O delimitador ';' NÃO deve ser alterado.
    """
    campos = linha.split(";")
    resultado = []

    for campo in campos:
        if "," in campo:
            partes = campo.split(",")
            if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
                campo = campo.replace(",", ".")
        resultado.append(campo)

    return ";".join(resultado)
