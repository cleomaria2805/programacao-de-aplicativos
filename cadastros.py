import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
''')

nome = input("nome completo: ")
telefone = int(input("seu telefone: "))
turma = int(input("sua turma: "))
idade = int(input("sua idade: "))
CPF = int(input("seu CPF: "))

comando_insert = f"""
INSERT INTO Alunos (nome, telefone, turma, idade, CPF) 
VALUES ('{nome}', '{telefone}', '{turma}', {idade}, '{CPF}');
"""
