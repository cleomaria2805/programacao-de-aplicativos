import sqlite3 
 
def verificar_registros(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL
                   )
                   ''')
    cursor.execute("SELECT * FROM alunos") 
     
    # CORREÇÃO: salva os dados em uma variável para reutilizá-los
    dados_alunos = cursor.fetchall()
    
    print("primeiro print:", dados_alunos) 
    print("segundo print:", dados_alunos) 
     
    conexao.close()