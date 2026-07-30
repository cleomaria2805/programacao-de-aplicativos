import sqlite3 
 
def vincular_aluno_turma(): 
    nome = input("nome do aluno: ") 
    conexao = None # CORREÇÂO: inicializa a variável para evitar erro no finally

    try: 
        id_turma = int(input("digite o ID numérico da turma: ")) 
         
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma)) 
        conexao.commit() 

    except ValueError:

        # CORREÇÂO: captura o erro caso o usuário não digite um número inteiro
        print("ERRO: Você deve digitar um número inteiro válido para o ID da turma!")

    except sqlite3.Error as erro:

         # captura erros exclusivos do banco de dados
        print(f"erro no banco de dados!: {erro}") 

    finally: 

         # CORREÇÂO: só fecha a conexão se ela tiver sido aberta com sucesso
        if conexao:
            conexao.close() 
 
