cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nome_da_cidde = input("Digite o nome de alguma cidade: ")
if nome_da_cidde in cidades:
    posicao = cidades.index(nome_da_cidde)
    print(f"A cidade {nome_da_cidde} está na posição {posicao}.")
else:
    print(f"A cidade {nome_da_cidde} não foi encontrada na lista.")