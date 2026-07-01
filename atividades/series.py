import sqlite3 

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')

    conexao.execute("PRAGMA foreign_keys = ON;")

    cursor = conexao.cursor()
    # o aluno tenta cadastrar uma serie com id_escola = 999 (que nao existe).
    #o SQlite aceita o cadastro mesmo assim. o que esta faltando ativar?
    print("Série cadastrada com sucesso!")
    try:
        cursor.execute("INSERT INTO series(nome_serie, id_escola) VALUES(?,?)",(nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: O ID da escola {id_escola} não existe.")
        # Aqui você pode tratar o erro (ex: avisar o usuário)
    finally:
        conexao.close()
