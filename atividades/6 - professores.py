import sqlite3 
 
def buscar_professor(id_prof): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

     # CORREÇÃO: adicionada a vírgula para transformar em uma tupla de 1 elemento
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof)) 

    resultado = cursor.fetchone() 

    if resultado:
        print(f"professor encontrado: {resultado[0]}") 
    else:
        print("professor não cadastrado.")
        
    conexao.close() 
