nome = input("digite o seu nome: ")
valor_todal_da_compra = float(input("digiteo valor da compra: "))
frete = int(input("digite a distancia da entrega: "))
cupom_especial = input("Voce possui cupom especial?(S/N): ")




if valor_todal_da_compra >= 1.000 and cupom_especial == "S":
    desconto = valor_todal_da_compra * 0.20
    valor = valor_todal_da_compra - desconto

elif valor_todal_da_compra > 500.00 and cupom_especial == "S":
    desconto = valor_todal_da_compra * 0.10
    valor = valor_todal_da_compra * 0.10
if valor_todal_da_compra >= 200.00 and frete >= 50:
    frete= 0
    valor_final = valor + frete 
else:
    valor_final = valor + frete


print("seu nome é: ", nome)
print("o valor da compra é: ", valor_todal_da_compra)
print("valor total é: ", valor)
print("valor final é: ", valor_final)
