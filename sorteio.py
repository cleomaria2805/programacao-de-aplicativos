id_do_usuario = int(input("digite o ID do usuario: "))
valor_da_compra = float(input("digite o valor da compra: "))

if id_do_usuario % 2 == 0 and valor_da_compra > 500.00:
    print(f"parabens, usuario {id_do_usuario} voce ganhou um cupom para sua compra de R$: {valor_da_compra}")
else:
    print(f"obrigado pela compra usuario {id_do_usuario} continue acompanhando nossas promoçoes")