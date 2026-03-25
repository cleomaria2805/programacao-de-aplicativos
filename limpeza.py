usuarios = ["admin", "convidado", "suporte", "teste"]
print(f"lista antiga: {usuarios}")
usuarios.remove("teste")
del usuarios[0]
print(f"lista atual: {usuarios}")