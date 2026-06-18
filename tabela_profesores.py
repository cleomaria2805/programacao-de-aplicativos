import sqlite3

def cadastrar_professor():

    conexao = sqlite3.connect('ecola_demonstracao.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL,
        salario REAL NOT NULL,
        escola TEXT NOT NULL
    )
''')
    
nome = input("seu nome completo: ")
telefone = int(input("seu telefone: "))
materia = input("sua materia: ")
idade = int(input("sua idade: "))
cpf = int(input("seu CPF: "))
salario = int(input("seu salario: "))
escola = input("sua escola: ")

comando_insert = """
INSERT INTO PROFESSORES (nome, telefone, materia, idade, cpf, salario, escola)
VALUES(?, ?, ?, ?, ?, ?, ?);
"""

def listar_professores():
    conexao = sqlite3.connect('ecola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professores")
    professores = cursor. fetchall()

    if not professores:
        print("nenhum professor encontrado!")
        conexao.close()
        return
    

    for prof in professores:
        print(f"ID: {prof[0]}")
        print(f"Nome: {prof[1]} | Tel: {prof[2]} | Matéria: {prof[3]}")
        print(f"Idade: {prof[4]} anos | CPF: {prof[5]}")
        print(f"Salário: R$ {prof[6]:.2f} | Escola: {prof[7]}")
        print("-" * 50)

    conexao.close()

def atualizar_professores():
    conexao = sqlite3.connect('ecola_demonstracao.db')
    cursor = conexao.cursor()

    id_busca = int(input("digite o id: "))

    cursor.execute(f''' SELECT * FROM professores WHERE id = {id_busca}''')
    professor = cursor.fetchone()
    if not professor:
        print("professor nao encontrado")
    
        conexao.close()
        return

    else:
        novo_nome = input("digite o novo nome: ")
        nova_idade = int(input("digite a nova idade: "))
        novo_telefone = int(input("digite o novo telefone: "))
        nova_materia = input("digite a nova matéria: ")
        novo_cpf = input("digite o novo CPF: ")
        novo_salario = float(input("digite o novo salário: "))
        nova_escola = input("digite a nova escola: ")

    comando =f"UPDATE professores set nome = '{novo_nome}', idade = '{nova_idade}', telefone = '{novo_telefone}', materia = '{nova_materia}' cpf = '{novo_cpf}', salario = '{novo_salario}', escola = '{nova_escola}'"
    id = {id_busca}

    cursor.execute(comando)
    conexao.commit()
    conexao.close

def excluir_professores():
    conexao = sqlite3.connect('ecola_demonstracao.db')
    cursor = conexao.cursor()

    id_busca = int(input("Digite o ID do professor que deseja excluir: "))
    cursor.execute(f'''DELETE FROM professores WHERE id = {id_busca}''')

    conexao.commit()
    conexao.close()

    print("professor excluído com sucesso!")

while opcao: 
    
    print("1 - cadastrar Professor")
    print("2 - listar Professores")
    print("3 - atualizar Professor")
    print("4 - excluir Professor")
    print("5 - sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1': cadastrar_professor()
    elif opcao == '2': listar_professores()
    elif opcao == '3': atualizar_professores()
    elif opcao == '4': excluir_professores()
    elif opcao == '5': print("Saindo do sistema...") 
    else: print("Opção inválida!")