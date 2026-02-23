# Condicionais -> estruturas if, else
idade = 17

# Estrutura do if
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Meia entrada -> menor de 18 OU esteja estudando em escola publica/faculdade
estuda_rede_publica = False
if idade < 18 or estuda_rede_publica:
    print("Você tem direito à meia entrada.")
else:
    print("Você não tem direito à meia entrada.")

# Utilizando elif -> else if
# Uma condição intermediária entre o if e o else
nota = 10

if nota > 9:
    print("O seu conceito é A")
elif nota > 8:
    print("O seu conceito é B")
elif nota > 7:
    print("O seu conceito é C")
else:
    print("Você deve melhorar a sua nota.")

# Climas: ensolarado, chuvoso e nublado
clima = "chuvoso"

if clima == "ensolarado":
    print("Hoje é um dia ensolarado")
elif clima == "chuvoso":
    print("Hoje é um dia chuvoso")
elif clima == "nublado":
    print("Hoje é um dia nublado")

# Comissão de vendas
# > 1000 = .5%
# > 500 = 1%
# = 2%

vendas = 1000

if vendas > 1000:
    comissao = vendas * 0.005
elif vendas > 500:
    comissao = vendas * 0.01
else:
    comissao = vendas * 0.02
print("A comissão é: R$", comissao)

# Baseado numa entrada do usuário, verifique se o número é maior que zero
numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é maior que zero:", numero)
else:
    print("O número é menor ou igual a zero:", numero)

#Exercicios
# 1 Verificando Se um Número é Positivo, Negativo ou Zero

numero1 = float(input("Digite um número: "))

if numero1 > 0:
    print("O número é positivo:", numero1)
elif numero1 < 0:
    print("O número é negativo:", numero1)
else:
    print("O número é zero:", numero1)

# 2 Calculadora Simples

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == "/":    
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")

# 3 Classificação de Idade

idade = int(input("Digite a idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade > 12 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else: 
    print("Idade inválida.")

# # 4 Verificando se um Ano é Bissexto

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(ano,"é bissexto.")
else:
    print(ano,"não é bissexto.")

# # 5 Simulador de Caixa Eletrônico

valor_saque = int(input("Digite o valor do saque: R$"))

if valor_saque <= 0:
    print("Valor inválido. O valor do saque deve ser maior que zero.")
else:
    notas_100 = valor_saque // 100
    valor_saque = valor_saque % 100

    notas_50 = valor_saque // 50
    valor_saque = valor_saque % 50

    notas_20 = valor_saque // 20
    valor_saque = valor_saque % 20

    notas_10 = valor_saque // 10
    valor_saque = valor_saque % 10

    notas_5 = valor_saque // 5
    valor_saque = valor_saque % 5

    notas_2 = valor_saque // 2
    valor_saque = valor_saque % 2

    if valor_saque != 0:
        print("Valor inválido. O caixa eletrônico só aceita valores múltiplos de 10.")
    else:
        print("Cédulas entregues:")
        if notas_100 > 0:
            print(f"{notas_100} x R$100")
        if notas_50 > 0:
            print(f"{notas_50} x R$50")
        if notas_20 > 0:
            print(f"{notas_20} x R$20")
        if notas_10 > 0:
            print(f"{notas_10} x R$10")
        if notas_5 > 0:
            print(f"{notas_5} x R$5")
        if notas_2 > 0:
            print(f"{notas_2} x R$2")

# Exercicios Extras
# 1 Aprovando Empréstimo Bancário

emprestimo = float(input("Digite o valor do empréstimo: R$"))
renda_mensal = float(input("Digite o seu salário mensal: R$"))
num_parcelas = int(input("Digite o número de parcelas: "))
valor_parcela = emprestimo / num_parcelas

if valor_parcela <= 0.3 * renda_mensal:
    print(f"Empréstimo aprovado! O valor da parcela é R${valor_parcela:.2f} em {num_parcelas} parcelas.")
else:
    print(f"Empréstimo negado. O valor da parcela R${valor_parcela} excede 30% da sua renda mensal.")

#  2 Jogo Pedra,Papelo ou Tesoura    

import random

opcoes = ["pedra", "papel", "tesoura"]
computador = random.choice(opcoes)
jogador = input("Escolha pedra, papel ou tesoura: ")
if jogador not in opcoes:
    print("Opção inválida. Por favor, escolha pedra, papel ou tesoura.")
else:
    if jogador == computador:
        print(f"Empate! O computador também escolheu {computador}.")
    elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
        print(f"Parabéns! Você venceu! O computador escolheu {computador}.")
    else:
        print(f"Você perdeu! O computador escolheu {computador}.")

# 3 Calculadora de Tarifas de Táxi

tarifa = 4
distancia = float(input("Digite a distância percorrida em km: "))

if distancia < 0:
    print("Distância inválida. Por favor, insira um valor positivo.")
else:
    preco_corrida = (distancia * 0.25) + tarifa
    print(f"O preço da corrida é: R${preco_corrida:.2f}")
