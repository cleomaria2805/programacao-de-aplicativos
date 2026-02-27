nivel = int(input("digite o nivel do presonagem: "))
esferas = int(input("digite a quantidade de esferas coletadas pelo personagem: "))

if nivel >= 20 and esferas >= 50:
    print("Habilidade super salto desbloqueado.")
elif nivel < 20 and esferas < 50:
    print("habilidades não desbloqueada")