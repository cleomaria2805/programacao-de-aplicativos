alunos = ["joao", "maria", "luna", "lucas", "luis"]
notas = [80, 60, 100, 54, 55]
for nota in notas:

    if nota >= 60:
        indice = notas.index(nota)
        print(alunos[indice])

print(f"nova atual:{alunos}")