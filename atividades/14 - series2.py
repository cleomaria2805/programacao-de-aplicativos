import sqlite3 
 
def cadastrar_serie_seguro(nome, id_escola): 
    try: 
        # CORREÇÃO: o 'with' gerencia a abertura e o fechamento automático com segurança

        with sqlite3.connect('/pasta_protegida/sistema.db') as conexao: 
            cursor = conexao.cursor() 
            cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola)) 
            conexao.commit() 
    except sqlite3.Error as e: 

        print("erro técnico:", e)