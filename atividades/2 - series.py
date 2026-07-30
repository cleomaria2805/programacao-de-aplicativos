import sqlite3 

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')

    conexao.execute("PRAGMA foreign_keys = ON;")

    cursor = conexao.cursor() 

     # CORREÇÂO: Falta ativar o PRAGMA foreign_keys = ON; aqui para o SQLite validar chaves estrangeiras.
    print("série cadastrada com sucesso!")

    try:
        cursor.execute("INSERT INTO series(nome_serie, id_escola) VALUES(?,?)",(nome_serie, id_escola))
        conexao.commit()

    except sqlite3.IntegrityError as e:

        print(f"erro de integridade: O ID da escola {id_escola} não existe.")
      
    finally:
        conexao.close()
