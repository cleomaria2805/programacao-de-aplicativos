ataque = float(input("digite o dano de ataque do heroi: "))
defesa = float(input("digite os pontos de defesa do vilao: "))

dano = ataque - defesa 

if dano <= 0:
    print("O vilao bloqueou o ataque! dano: 0")
elif dano > 0:
    print("Ataque critico! você causou dano no vilao de", dano)