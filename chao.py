curso = input("o aluno concluiu o curso de segurança?(s/n): ")

if curso == "n":
    print("acesso negado!: faça o treinamento primeiro.")

elif curso == "s":
    instrutor = input("o instrutor esta presente na sala? (s/n): ")
    if instrutor == "s":
        print("acesso liberado!: operação iniciada")
    else: 
        print("aguarde o instrutor para ligar a maquina.")