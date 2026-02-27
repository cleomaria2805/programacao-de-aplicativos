nota = float(input("digite a nota do aluno: "))
presença = int(input("digite a presença do aluno: "))

if nota >= 7.0 and presença > 75.0:
    print("parabéns! você foi aprovado.")
elif nota < 7.0 and presença < 75.0:
    print("reprovado. verifique sua nota a presença")