def e_par(numero):
    """Retorna True se o número for par e False se for ímpar."""
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número inteiro: "))

if e_par(num):
    print("Este número é par")
else:
    print("Este número é ímpar")