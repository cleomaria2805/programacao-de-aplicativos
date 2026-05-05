def converter_km_em_ms(velocidade_km):
    return velocidade_km / 3.6

velocidade = float(input("digite a velocidade em km/h: "))

if velocidade > 80:
    velocidade_ms = converter_km_em_ms(velocidade)
    print(f"velocidade em m/s: ")
    print("reduza a velocidade!")
else:
    print("velocidade dentro do limite.")