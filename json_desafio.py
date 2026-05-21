import json
import os

def criar_arquivo():
    open("dados.json", 'w').close()
criar_arquivo()

def criar_usuario():
    cpf = int(input("digite seu cpf: "))
    nome = input("digite seu nome: ")
    telefone = int(input("digite seu telefone: "))
    turma = int(input("digite sua turma: "))
    idade = int(input("digite sua idade: "))

    aluno = {
        "CPF" : cpf,
        "nome" : nome,
        "telefone" : telefone,
        "turma" : turma,
        "idade" : idade,
        }
    with open("dados.json" , 'r') as arquivo:
        dados = json.load(arquivo)
    
    dados.append(aluno)
    
    
    with open("dados.json" , 'w') as arquivo:
        json.dump(aluno, arquivo, indent=4)
        print(f"aluno criado com sucesso!")

criar_usuario()
