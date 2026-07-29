import sqlite3 
 
def vincular_aluno_turma(): 
    nome = input("Nome do aluno: ") 
    conexao = None 

    try: 
        id_turma = int(input("Digite o ID numérico da turma: ")) 
         
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma)) 
        conexao.commit() 

    except ValueError:
        print("Erro: Você deve digitar um número inteiro válido para o ID da turma!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!: {erro}") 

    finally: 
        if conexao:
            conexao.close() 
 
