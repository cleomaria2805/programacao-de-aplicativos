pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"]
concluidos = []
print(f"arquivo antigo do pendentes: {pendentes} e concluidos: {concluidos}")
pendentes.pop(0)
concluidos.append("Relatorio.pdf")
print(f"arquivo atual do pendentes:{pendentes} e concluidos: {concluidos}")