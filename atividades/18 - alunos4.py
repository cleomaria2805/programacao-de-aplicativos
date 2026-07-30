import sqlite3 
 
def cadastrar_lista_alunos(): 
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)] 
     
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   id_turma INTEGER)''')
    
    # CORREÇÃO: alterado de .execute() para .executemany()
    cursor.executemany("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", lista) 
     
    conexao.commit() 
    conexao.close()

    cadastrar_lista_alunos()