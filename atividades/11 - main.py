import sqlite3 
 
def listar_alunos_e_turmas(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    # CORREÇÃO: adicionada a cláusula ON para vincular a chave estrangeira à chave primária
    cursor.execute("""
        SELECT alunos.nome, turmas.nome_turma 
        FROM alunos 
        INNER JOIN turmas ON alunos.id_turma = turmas.id
    """) 
     
    for linha in cursor.fetchall(): 
        print(f"aluno: {linha[0]} | turma: {linha[1]}") 
    conexao.close()