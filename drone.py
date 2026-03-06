print("- Fase de Indentificação -")
codigo = int(input("digite o codigo do drone: "))
autorização = input("O drone possui autorização de Torre (s/n): ")

if codigo == 999 or autorização == "s":
    print("tudo certo: Iremos avançar para analise de pouso.")


    print("- fase de analise de voo -")
    bateria = float(input("digite o nivel de bateria do drone: "))
    clima = input("qual o clima no momento: ")
    velocidade_do_vento = float(input("digite a velocidade do vento (k/m): "))

    if bateria < 10:
        print("EMERGENCIA: pouse imediatamente!")
    elif bateria >= 10 and clima == "ensolarado" and (velocidade_do_vento < 30 or clima == "chuvoso") and velocidade_do_vento < 10:
        print("POUSO ALTORIZADO: iniciando decida")
    else:
        print("POUSO NEGADO: condições metereologicas perigosas. Aguarde em orbita")

else:
    print("ERRO 01: drone nao indentificado. retornar a base.")