import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    limpar_tela()

    print("=== CALCULADORA DE CONSUMO DE ENERGIA ===")
    print("")

    nome = input("Informe o nome do aparelho: ")

    try:
        potencia = float(input("Informe a potência do aparelho em watts (W): "))
        horasDia = float(input("Informe o tempo médio de uso diário em horas: "))
    except ValueError:
        print("")
        print("Erro: digite apenas números válidos para potência e horas de uso.")
        print("")
        repetir = input("Deseja tentar novamente? (S/N): ").lower()

        if repetir != "s":
            limpar_tela()
            print("Calculadora encerrada. Até a próxima!")
            break

        continue

    # Impede que valores inválidos sejam utilizados no cálculo
    if potencia <= 0 or horasDia <= 0:
        print("")
        print("Erro: a potência e o tempo de uso devem ser maiores que zero.")

    else:
        # Calcula uma estimativa do consumo mensal do aparelho em kWh
        consumoMensal = (potencia * horasDia * 30) / 1000

        # Tarifa fixa utilizada para estimar o custo mensal de energia
        tarifa = 0.75

        custoMensal = consumoMensal * tarifa

        limpar_tela()

        print("=== RESULTADO DA ESTIMATIVA ===")
        print("")
        print(f"Aparelho: {nome}")
        print(f"Consumo mensal estimado: {consumoMensal:.2f} kWh/mês")
        print(f"Custo mensal estimado: R$ {custoMensal:.2f}")
        print("Tarifa utilizada no cálculo: R$ 0,75 por kWh")

    print("")
    repetir = input("Deseja calcular o consumo de outro aparelho? (S/N): ").lower()

    if repetir != "s":
        limpar_tela()
        print("Calculadora encerrada. Até a próxima!")
        break
