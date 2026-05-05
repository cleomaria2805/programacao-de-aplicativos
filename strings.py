def contar_caracteres(texto):
    """"retorna o tamanho da string recebida."""
    return len(texto)

usuario = input("digite seu nome de usuário: ")
tamanho = contar_caracteres(usuario)

if tamanho < 5:
    print("nome de usuário muito curto")
else:
    print("nome aceito")