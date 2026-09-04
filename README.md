# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Energia](https://img.shields.io/badge/Energia-Consumo%20Elétrico-yellow)

## 📌 Sobre o projeto

A **Calculadora de Consumo de Energia** é um programa desenvolvido para estimar o consumo mensal de energia elétrica de um aparelho a partir da potência informada e do tempo médio de uso diário.

Além do consumo em kWh, o sistema apresenta uma estimativa de custo mensal utilizando uma tarifa fixa de **R$ 0,75 por kWh**.

## 🧮 Fórmula utilizada

```text
consumoMensal = (potencia * horasDia * 30) / 1000
```

Onde:

- `potencia`: potência do aparelho em watts (W)
- `horasDia`: tempo médio de uso diário em horas
- `30`: quantidade média de dias no mês
- `1000`: conversão de watts para quilowatts

Para calcular o custo mensal estimado, o programa utiliza:

```text
custoMensal = consumoMensal * 0.75
```

## 🧠 Evolução do projeto

O projeto foi iniciado em **VisuAlg**, com a criação da lógica principal do algoritmo. Depois, essa lógica foi adaptada para **Python**, mantendo a mesma ideia de entrada de dados, validação e cálculo do consumo.

Essa etapa mostra a evolução do raciocínio lógico para a implementação em uma linguagem de programação.

## 🛠️ Tecnologias utilizadas

- Visualg
- Python 3.x
- Git
- GitHub

## 📂 Estrutura do projeto

```text
consumo-energia/
├── algoritmo_visualg.alg
├── app.py
└── README.md
```

## 📄 Arquivos principais

- `algoritmo_visualg.alg`: versão inicial da lógica feita em VisuAlg.
- `app.py`: versão final do programa desenvolvida em Python.
- `README.md`: documentação do projeto.

## ▶️ Como executar

1. Tenha o Python instalado no computador.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python app.py
```

## 💡 Exemplo de uso

```text
Informe o nome do aparelho: Geladeira
Informe a potência do aparelho em watts (W): 150
Informe o tempo médio de uso diário em horas: 10

Aparelho: Geladeira
Consumo mensal estimado: 45.00 kWh/mês
Custo mensal estimado: R$ 33.75
Tarifa utilizada no cálculo: R$ 0,75 por kWh
```

## ✅ Funcionalidades

- Solicita o nome do aparelho.
- Solicita a potência em watts.
- Solicita o tempo médio de uso diário.
- Calcula o consumo mensal em kWh.
- Calcula uma estimativa de custo mensal.
- Permite calcular o consumo de vários aparelhos em sequência.

## 👨‍💻 Autor

Projeto desenvolvido para atividade acadêmica de Desenvolvimento de Sistemas.
