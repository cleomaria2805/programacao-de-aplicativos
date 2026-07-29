import sqlite3 
 
def buscar_professor(id_prof): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof)) 

    resultado = cursor.fetchone() 

    if resultado:
        print(f"professor encontrado: {resultado[0]}") 
    else:
        print("professor não cadastrado.")
        
    conexao.close() 
