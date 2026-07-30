import sqlite3

def iniciar_banco():

    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
        )
    ''')
    conexao.commit  # CORREÇÂO: Faltou chamar conexao.commit()
    conexao.close()
