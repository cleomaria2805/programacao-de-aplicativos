usuario = input("digite o seu nome de usuario: ")
codigo = int(input("digite o seu codigo: "))

if usuario == "adimin" and codigo == 999:
    print("Acesso ao servidor liberado. Sistema online.")
else:
    print("falha na autenticação. alerta de segurança ligado.")
