import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # CORREÇÃO: Criar a tabela 'escolas' primeiro
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS escolas ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT 
        ) 
    ''') 

     # Agora a tabela 'series' pode referenciar 'escolas' sem erros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_serie TEXT NOT NULL,
        id_escola INTEGER,
        FOREIGN KEY (id_escola) REFERENCES escolas(id)
    )
    ''')
    conexao.commit() 
    conexao.close()