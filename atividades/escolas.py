import sqlite3

def cadastrar_escola_rapido():
    nome = input("digite o nome da escola: ")
    endereco =input("digite o endereço: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    