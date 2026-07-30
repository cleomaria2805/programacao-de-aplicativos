def menu(): 
    while True: 
        print("1. cadastrar Aluno") 
        print("2. sair") 
        opcao = input("escolha: ") 
         
        if opcao == "1": 
            print("cadastrando...") 
        elif opcao == "2": 
            print("saindo do programa.") 
            break  # CORREÇÃO: interrompe o loop while e encerra o menu