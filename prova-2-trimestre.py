import sqlite3

def cadastrar_distribuidora():

        conexao = sqlite3.connect("sistema.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS distribuidoras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_distribuidora TEXT NOT NULL,
                licenca_anvisa TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS farmacias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endereco TEXT NOT NULL,
                id_distribuidora INTEGER NOT NULL,
                FOREIGN KEY (id_distribuidora) REFERENCES distribuidoras(id)
            )
        """)
        conexao.commit()

id_distribuidora = int(input("ID da distribuidora: "))
nome_distribuidora = input("nome: ")
licença_distribuidora = input("licença: ")

def listar_distribuidora():
    conexao = sqlite3.connect('distribuidora.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM distribuidoras")
    distribuidora = cursor. fetchall()

    if not distribuidora:
        print("nenhuma distribuidora encontrada!")
        conexao.close()
        return
    for dis in distribuidora:
        print(f"ID: {dis[0]}")
        print(f"nome: {dis[1]} | licença: {dis[2]}")
        print("-" * 50)

    cursor.execute("""
    INSERT INTO distribuidoras
    (nome_distribuidora, licenca_distribuidora)
    VALUES (?, ?)
""", (nome_distribuidora, licença_distribuidora))

def atualizar_distribuidora():
    conexao = sqlite3.connect('distribuidora.db')
    cursor = conexao.cursor()

    id_busca = int(input("digite o id: "))

    cursor.execute(f'''SELECT * FROM distribuidoras WHERE id = ? UPDATE distribuidoras
SET nome_distribuidora = ?, licenca_distribuidora = ? WHERE id = ?''')

    distribuidora = cursor.fetchone()
    if not distribuidora:
        print("distribuidora nao encontrada!")
    
        conexao.close()
        return
    else:
        novo_id_distribuidora = int(input("digite o novo id da distribuidora"))
        novo_nome = input("digite o novo nome: ")
        nova_licença_distribuidora = int(input("digite a nova licença"))

    comando =f"UPDATE professores set nome = '{novo_nome}', ID = '{novo_id_distribuidora}', licença = '{nova_licença_distribuidora}'"

    cursor.execute(comando)
    conexao.commit()
    conexao.close

def excluir_distribuidora():
    conexao = sqlite3.connect('distribuidora.db')
    cursor = conexao.cursor()

    id_busca = int(input("Digite o ID da distribuidora que deseja excluir: "))
    cursor.execute(f'''DELETE FROM distribuidoras''')

    conexao.commit()
    conexao.close()

    print("distribuidora excluida com sucesso!")

opcao = 0

while opcao != 5:
    print("1 -- cadastrar")
    print("2 -- listar")
    print("3 -- atualizar")
    print("4 -- excluir")
    print("5 -- sair")

    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1:
        cadastrar_distribuidora()
    elif opcao == 2:
        listar_distribuidora()
    elif opcao == 3:
        atualizar_distribuidora()
    elif opcao == 4:
        excluir_distribuidora()
    elif opcao == 5:
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")

def cadastrar_farmacia():
    conexao = sqlite3.connect("sistema.db")
    cursor = conexao.cursor()

id_distribuidora = int(input("ID da distribuidora: "))
nome_distribuidora = input("nome: ")
licença_distribuidora = input("licença: ")

def listar_farmacias():
    try:
        conectar = ("nn sei")
        conexao = conectar()

        if conexao is None:
            return

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                farmacias.id,
                farmacias.endereco,
                farmacias.id_distribuidora,
                distribuidoras.nome_distribuidora
            FROM farmacias
            INNER JOIN distribuidoras
            ON farmacias.id_distribuidora = distribuidoras.id
        """)

        farmacias = cursor.fetchall()

        conexao.close()

        if len(farmacias) == 0:
            print("Nenhuma farmácia cadastrada.")
        else:
            print("\n--- FARMÁCIAS ---")

            for farmacia in farmacias:
                print(
                    "ID:", farmacia[0],
                    "| Endereço:", farmacia[1],
                    "| ID Distribuidora:", farmacia[2],
                    "| Distribuidora:", farmacia[3]
                )

    except sqlite3.Error as erro:
        print("Erro ao listar farmácias:", erro)
    except (ValueError, TypeError) as erro:
        print("Entrada inválida:", erro)


def atualizar_farmacia():
    try:
        id_farmacia = int(
            input("ID da farmácia que deseja atualizar: ")
        )
        endereco = input("Novo endereço: ")
        id_distribuidora = int(
            input("Novo ID da distribuidora: ")
        )
        conectar = ("nn sei")
        conexao = conectar()
        if conexao is None:
            return
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id FROM farmacias WHERE id = ?",
            (id_farmacia,)
        )
        if cursor.fetchone() is None:
            print("Farmácia não encontrada.")
            conexao.close()
            return
        cursor.execute(
            "SELECT id FROM distribuidoras WHERE id = ?",
            (id_distribuidora,)
        )
        if cursor.fetchone() is None:
            print("A distribuidora informada não existe.")
            conexao.close()
            return
        cursor.execute("""
            UPDATE farmacias
            SET endereco = ?, id_distribuidora = ?
            WHERE id = ?
        """, (endereco, id_distribuidora, id_farmacia))
        conexao.commit()
        conexao.close()

        print("Farmácia atualizada com sucesso!")

    except ValueError:
        print("Digite IDs válidos.")
    except sqlite3.Error as erro:
        print("Erro ao atualizar farmácia:", erro)
    except (TypeError, AttributeError) as erro:
        print("Entrada inválida:", erro)


def excluir_farmacia():
    try:
        id_farmacia = int(
            input("ID da farmácia que deseja excluir: ")
        )
        conectar = ("nn sei")
        conexao = conectar()
        if conexao is None:
            return
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id FROM farmacias WHERE id = ?",
            (id_farmacia,)
        )
        if cursor.fetchone() is None:
            print("Farmácia não encontrada.")
            conexao.close()
            return
        cursor.execute(
            "DELETE FROM farmacias WHERE id = ?",
            (id_farmacia,)
        )
        conexao.commit()
        conexao.close()

        print("Farmácia excluída com sucesso!")

    except ValueError:
        print("Digite um ID válido.")
    except sqlite3.Error as erro:
        print("Erro ao excluir farmácia:", erro)
    except (TypeError, AttributeError) as erro:
        print("Entrada inválida:", erro)


def menu():
        while True:
            print("\n========== MENU ==========")
            print("1 - Cadastrar distribuidora")
            print("2 - Listar distribuidoras")
            print("3 - Atualizar distribuidora")
            print("4 - Excluir distribuidora")
            print("5 - Cadastrar farmácia")
            print("6 - Listar farmácias")
            print("7 - Atualizar farmácia")
            print("8 - Excluir farmácia")
            print("0 - Sair")
            print("==========================")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_farmacia()
            elif opcao == "2":
                listar_farmacias()
            elif opcao == "3":
                atualizar_farmacia()
            elif opcao == "4":
                excluir_farmacia()
            else:
                print("Opção inválida.")



