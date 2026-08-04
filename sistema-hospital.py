import sqlite3

try:
    conexao = sqlite3.connect("hospital.db")
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""CREATE TABLE IF NOT EXISTS hospital (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               cidade TEXT NOT NULL
               )
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS medicos (
               id INTEGER PRIMARY KEY AUTOINCEMENT,
               nome TEXT NOT NULL,
               crm TEXT NOT NULL UNIQUE,
               id_hospital INTEGER NOT NULL)
               FOREIGN KEY (id_hospital) REFERENCES hospitais (id)
        )
""")

conexao.commit()

cursor.execute("SELECT COUNT (*) FROM hospitais")
if cursor.fetchall()[0] == 0:
    cursor.execute(
        "INSERT INTO hospitais (nome, cidade) VALUES (?,?),"
        ("Hospital", "São Paulo")
    )

conexao.commit()

print("---Cadastrar Medico: ---")
nome_medico = print("digite o nome do medico: ")
crm = print("digite o crm do medico: ")
id_hsp = print("digite o id do hospital: ")

cursor.execute("INSERT INTO medicos (nome, crm, id_hospital) VALUES (?,?),"
               (nome_medico, crm, id_hsp),
               )
conexao.commit()

print("medico cadastrado com sucesso! ")

