lista_secreta = ["123"]
tentativas = 0
acertou = False
while tentativas < 3 and not acertou:
    palpite = input("tente adivinha a senha: ")

    if palpite in lista_secreta:
        print("acesso liberado!")
        acertou = True
    else:
        print("senha incorreta")

    tentativas += 1
if not acertou:
    print("suas tentativas acabaram.")
    print(f"a senha era: {lista_secreta}")