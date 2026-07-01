import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #este bloco quebra ao rodar pela primeira vez em um banco limpo. porque?

        # Corrigido de AUTPINCREMENT para AUTOINCREMENT
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS series (  
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_serie TEXT,
        id_escola INTEGER,
        FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    ''')

conexao.commit()
conexao.close()