valor = float(input("qual é o valor da compra? R$:"))
if valor > 100.00:
    desconto = valor * 0.10
    final = valor - desconto
    print(f"sua compra teve um desconto: R${final}")
else:
    print(f"valor de sua compra: R${valor}")