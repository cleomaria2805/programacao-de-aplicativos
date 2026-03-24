nomes = ["Alice", "Bob", "Carlos"]
entradads_de_dados = input("digite o nome de algum pesquisador: ")
if entradads_de_dados in nomes:
    print(f"Acesso Permitido! O pesquisador {entradads_de_dados} está na posição", nomes.index(entradads_de_dados))
    pergunta = input("deseja remover esse pesquisador da lista? (s/n): ")
    if pergunta == "s":
        nomes.remove(entradads_de_dados)
        print(f"lista atualizada: {nomes}")
    else:
        print("encerrando o programa.")

else:
    print( f"Acesso Negado! O pesquisador {nomes} não foi encontrado.")
    pergunta2 = input(f"deseja cadastrar esse novo pesquisador? (s/n):" )
    if pergunta2 == "s":
        nomes.append(entradads_de_dados)
        print(f"lista autorizada {entradads_de_dados}")
    else:
        print("encerrndo o programa...")