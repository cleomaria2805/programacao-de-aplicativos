import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS series (  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_serie TEXT,
        id_escola INTEGER,
        FOREIGN KEY (id_escola) REFERENCES escolas(id)

                   import sqlite3 
 
	''') 
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