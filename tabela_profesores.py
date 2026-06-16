import sqlite3

def cadastrar_professor():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL,
        salario REAL NOT NULL,
        escola TEXT NOT NULL
    )
''')
    
nome = input("seu nome completo: ")
telefone = int(input("seu telefone: "))
materia = input("sua materia: ")
idade = int(input("sua idade: "))
cpf = int(input("seu CPF: "))
salario = int(input("seu salario: "))
escola = input("sua escola: ")

comando_insert = f"""
INSERT INTO PROFESSOR (nome, telefone, materia, idade, cpf, salario, escola)
VALUES('{nome}','{telefone}','{materia}','{idade}','{cpf}','{salario}','{escola}');
"""

cursor.execute(comando_insert)
conexao.commit()