def somar_carrinho(lista_de_preco):

    total = 0.0
    for preco in lista_de_preco:
        total += preco

    if total > 500:
        desconto = total * 0.10
        total -= desconto
        print(f"desconto de 10% aplicado: {desconto}")
        
    return total

carrinho = [150.00, 200.00, 300.00]

valor_final = somar_carrinho(carrinho)
print(f"o valor total da compra é: {valor_final}")