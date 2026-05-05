def somar_carrinho(lista_precos):
    total = sum(lista_precos)

    if total > 500:
        total = total * 0.90
        return total
    
carrinho = [150.00, 200.00, 300.00]

valor_final = somar_carrinho(carrinho)

print(f"O valor total da compra (com descontos aplicados, se houver) é: R$ {valor_final}")