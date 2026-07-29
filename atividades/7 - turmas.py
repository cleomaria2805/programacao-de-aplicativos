import sqlite3 
 
def cadastrar_turma(nome, id_serie, id_prof): 
    conexao = None
    try:
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("PRAGMA foreign_keys = ON;") 
         
        cursor.execute(
            "INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", 
            (nome, id_serie, id_prof)
        ) 
        conexao.commit() 
        print("Turma cadastrada com sucesso!")
        
    except sqlite3.IntegrityError:
        print("Erro: ID da série ou ID do professor inválido (Violação de Chave Estrangeira)!")
    except sqlite3.Error as erro:
        print(f"Erro genérico no banco de dados: {erro}")
        
    finally: 
        
        if conexao:
            conexao.close()