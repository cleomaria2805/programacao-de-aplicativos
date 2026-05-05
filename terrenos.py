def calcular_area(largura, comprimento):
    area = largura * comprimento
    return area

print("--- calculador de terreno ---")

contador = 1
while contador <= 3:
    print(f"terreno {contador}:")

    largura = float(input("Digite a largura (m): "))
    comprimento = float(input("Digite o comprimento (m): "))

    area_final = calcular_area(largura, comprimento)
    print(f"A área deste terreno é: {area_final} m²")

    contador += 1

    print("Por favor, digite números válidos.")

print("Cálculos finalizados.")