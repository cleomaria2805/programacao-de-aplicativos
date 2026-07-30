import sqlite3 
 
def deletar_escola_antiga(): 
    id_escola = int(input("ID da escola a remover: ")) 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    # CORREÇÃO: usando '?' para passar a variável do Python com segurança
    cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,)) 
     
    conexao.commit() 
    conexao.close()