idade = int(input("digite sa idade: "))
ingresso = input("digite se você tem ingresso (s/n): ")
lista = input("digite se você esta na lista (s/n): ")


if idade >= 18 and (ingresso == "s" or lista == "s"):
    print("seja bem-vindo/a")
else:
    print("você não tem acesso")