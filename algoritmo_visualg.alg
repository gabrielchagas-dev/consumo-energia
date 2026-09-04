algoritmo "Calculadora de Consumo de Energia"

var
nome: caractere
potencia, horasDia, consumoMensal, valorKwh, custo: real
repetir: caractere

inicio

repetir <- "S"

enquanto (repetir = "S") ou (repetir = "s") faca

  limpatela

  escreval("=== CALCULADORA DE CONSUMO DE ENERGIA ===")
  escreval("")

  escreva("Digite o nome do aparelho: ")
  leia(nome)

  escreva("Digite a potência do aparelho em Watts: ")
  leia(potencia)

  escreva("Digite o tempo médio de uso diário em horas: ")
  leia(horasDia)

  se (potencia <= 0) ou (horasDia <= 0) entao

     escreval("")
     escreval("Erro: a potência e o tempo de uso devem ser maiores que zero.")

  senao

     consumoMensal <- (potencia * horasDia * 30) / 1000

     valorKwh <- 0.75
     custo <- consumoMensal * valorKwh

     limpatela

     escreval("=== RESULTADO DA ESTIMATIVA ===")
     escreval("")
     escreval("Aparelho: ", nome)
     escreval("Consumo mensal estimado: ", consumoMensal:0:2, " kWh/mês")
     escreval("Custo mensal estimado: R$ ", custo:0:2)
     escreval("Tarifa utilizada no cálculo: R$ 0,75 por kWh")

  fimse

  escreval("")
  escreva("Deseja calcular o consumo de outro aparelho? (S/N): ")
  leia(repetir)

fimenquanto

limpatela
escreval("Calculadora encerrada. Até a próxima!")

fimalgoritmo
