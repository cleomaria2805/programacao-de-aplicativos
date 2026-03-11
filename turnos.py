id = int(input("digite o seu ID: "))
temperatura = float(input("digite a temperatura da maquina: "))
tempo_de_uso = float(input("digite a temperatura da maquina: "))

if (id % 3 == 0) and (temperatura > 40 or tempo_de_uso > 8):
    print(f"funcionario {id}. voce foi escalado para a manutenção preventiva hoje.")
else:
    print(f"funcionario {id}, sua maquina opera dentro dos pradoes normais")