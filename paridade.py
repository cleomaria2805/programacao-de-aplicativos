def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

usuario = int(input("digite um numero inteiro: "))

if eh_par(usuario):
    print("esse numero é par! ")
else:
    print("esse numero é impar")
