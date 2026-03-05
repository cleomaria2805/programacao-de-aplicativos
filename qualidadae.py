comprimento_da_peca = input("o comprimento da peça esta entre 10cm e 12cm (s/n): ")

if comprimento_da_peca == "n":
    print("reprovado!: problema no comprimneto. ")

elif comprimento_da_peca == "s":
        largura = input("a largura da peça esta entre 5cm e 6cm? (s/n): ")
        if largura == "s":
            print("peça aprovada!")
        else:
            print("reprovado!: problema na largura")