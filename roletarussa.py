senha = input("digite a senha: ")
tentativa = int(input("digite o numero de tentativas: "))
token = input("digite se voce tem token (s/n): ")

if (senha == "adimin123" and tentativa % 3 == 0) or (token == "s"):
    print(f"tentativa n°{tentativa}: ACESSO CONCEDIDO.")
else:
    print(f"tentativa n°{tentativa}: ACESSO CONCEDIDO.")