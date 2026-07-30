import sqlite3 
 
def cadastrar_professor(nome, cpf): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
     # CORREÇÃO: adicionado UNIQUE na coluna cpf
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS professores ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL, 
            cpf TEXT UNIQUE NOT NULL 
        ) 
    ''') 
    