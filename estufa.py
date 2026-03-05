temperatura = float(input("digite a temperatura atual do ambiente: "))

if temperatura <= 30:
    print("clima estavel. ")

elif temperatura > 30:
    print("alerta de calor!:")
    umidade = float(input("digite a umidade do ambiente: "))
    if umidade < 40:
        print("ação: ligar irrigação.")
    else:
        print("ação: ligar apenas os ventiladores")