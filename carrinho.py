produtos = []
entrada = ""

while entrada != "sair":
    entrada = input("digite o produto ou digite (sair) para sair.")

    if entrada != "sair":
        produtos.append(entrada)

print(f"sua lista de produtos {produtos}")
