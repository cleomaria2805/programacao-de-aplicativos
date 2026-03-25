livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []

emprestimo = input("digite o livro que deseja: ")
if emprestimo in livros_disponiveis:
    livros_disponiveis.remove(emprestimo)
    livros_emprestados.append(emprestimo)
    print("empréstimo realizado com sucesso!")
else:
    print("desculpe, esse livro não esta no acesso")

if len(livros_disponiveis) >= 2:
    del livros_disponiveis[0:2]
print(f"livros disponiveis: {livros_disponiveis}")
print(f"livros emprestados: {livros_emprestados}")