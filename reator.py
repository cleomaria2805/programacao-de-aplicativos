cargo_do_funcionario = input("digite seu cargo: ")
codigo_de_acesso = input("digite seu codigo de acesso: ")
botao_de_emergencia = input("o botão de emergencia foi precionado (s/n): ")
equipamento_de_protecao = input("seu equipamento de proteção (EPI) esta completo? (s/n): ")

if (cargo_do_funcionario == "engenheiro" or cargo_do_funcionario == "tecnico") and (codigo_de_acesso == "1234" or botao_de_emergencia == "s") and equipamento_de_protecao == "s":
    print("acesso liberado!")
else:
    print("acesso negado!: risco de segurança")