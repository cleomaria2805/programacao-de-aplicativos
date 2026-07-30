import sqlite3  
 
def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    cursor.execute('''CREATE TABLE IF NOT EXISTS escolas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT
                   )
                   ''')

    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,)) 
    conexao.commit() 
    print("adicionado")

nome = "maria"

inserir_escola(nome)
# CORREÇÃO: abra e feche a conexão sempre DENTRO de cada função.