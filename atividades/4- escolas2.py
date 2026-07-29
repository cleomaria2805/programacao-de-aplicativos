import sqlite3 
 
def cadastrar_escola_rapido(): 
	
    nome = input("digite o nome da escola: ") 
    endereco = input("digite o endereço: ") 
     
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute(f"INSERT INTO escolas (nome, endereco) VALUES ('?', '?')",(nome, endereco)) 
     
    conexao.commit() 
    conexao.close() 

    print(f"\n[Sucesso] escola '{nome}' cadastrada com sucesso!")
cadastrar_escola_rapido()