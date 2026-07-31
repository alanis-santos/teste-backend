def calcular_total_carrinho(carrinho: list[dict]) -> float:
    """
    Recebe uma lista de itens no formato:
        {"item": str, "preco": float, "quantidade": int}

    Retorna o valor total da compra (soma de preco * quantidade).
    Carrinho vazio deve retornar 0.0.
    """
    return float(sum(item["preco"] * item["quantidade"] for item in carrinho))
