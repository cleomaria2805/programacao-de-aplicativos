saldo_inicial = 1.000
print("1 - deposito, 2 - saque, 3 - extrato.")
menu = int(input("escolha uma opção: "))

if menu == 1:
    valor = float(input("digite o valor para depósito: "))
    if valor > 0:
        saldo_inicial = saldo_inicial + valor
        print("depósito realizado com sucesso!")
    else:
        print("valor inválido para depósito.")
        
    print("saldo atual: :", valor)

elif menu == 2:
    valor = float(input("digite o valor para saque: "))
    
    if valor > 0 and (valor <= saldo_inicial or valor == 100):
        saldo_inicial = saldo_inicial - valor
        print("saque realizado com sucesso!")
    else:
        print("saque não autorizado.")
        
    print("saldo atual: ", saldo_inicial)
elif menu == 3:
    print("saldo atual: = ", saldo_inicial)

else:
    print("opção inválida.")