import sqlite3 
 
def atualizar_nome_aluno(id_aluno, novo_nome): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    # CORREÇÃO: adicionada a cláusula WHERE e o id_aluno nos parâmetros
    cursor.execute("UPDATE alunos SET nome = ? WHERE id = ?", (novo_nome, id_aluno)) 
     
    conexao.commit() 
    conexao.close()