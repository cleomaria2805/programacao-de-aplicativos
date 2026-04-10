peso = float(input("digite seu peso em kg: "))
altura = float(input("digite sua altura em metros: "))

imc = peso / (altura * 2)

if imc > 25:
    print("você esta acima do peso. ")
else:
    print("voce está abaixo do peso. ")
