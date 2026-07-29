import sqlite3 
 
def cadastrar_professor(nome, cpf): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS professores ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL, 
            cpf TEXT UNIQUE NOT NULL 
        ) 
    ''') 
    
    try:
        cursor.execute("INSERT INTO professores (nome, cpf) VALUES (?, ?)", (nome, cpf))
        conexao.commit()
        print(f"Professor(a) '{nome}' cadastrado com sucesso!")
        
    except sqlite3.IntegrityError:
        print(f"Erro: O CPF '{cpf}' já está cadastrado para outro professor!")
        
    finally:
        conexao.close()