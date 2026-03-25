compras = []
item = ""
while item != "fim":
    item = input("Produto (ou 'fim'): ")
    if item != "fim":
        compras.append(item)
for i in compras:
    print(f"- {i}")