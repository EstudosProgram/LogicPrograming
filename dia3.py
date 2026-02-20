# 1 Calculando o troco
pao = 3.50
leite = 4.20
cafe = 2.80
valor_pago = 20
total = pao + leite + cafe
troco = valor_pago - total
print("O total da compra é: R$",total)
print("O troco é: R$",troco) 

# 2 Verificando Aprovação em um Exame
nota_media = 8.5
frequencia = 80
aprovado = (nota_media >= 7) and (frequencia >=75)
print("O aluno foi aprovado?", aprovado)

# 3 Oferta Especial
qnt_itens = 8
valor_total = 120
desconto = (qnt_itens > 10) or (valor_total > 100)
print("O cliente tem direito ao desconto?", desconto)

# 4 Sistema de Acesso
senha_inserida = "abcd1234"
senha_correta = "abcd1234"
user_bloc = False
acesso_permitido = (senha_inserida == senha_correta and not user_bloc)
print("Acesso permitido?", acesso_permitido)

# 5 DivisãodeTarefas
conta = 150.00
amigos = 2
valor_pessoa = conta / amigos
divisao_exata = (conta % amigos) == 0
print("Cada pessoa deve pagar: R$", valor_pessoa)
print("A divisão é exata?",divisao_exata)

# 6 Classificação Etária
idade = int(input("Qual a sua idade? "))
pode_assistir = idade >= 16 
print("Você pode assistir ao filme?",pode_assistir)

# 7 Calculadora de IMC
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura ** 2)
imc_adequado = (imc >= 18.5) and (imc <= 24.9)
print("O seu IMC é:",imc)
print("O seu peso está adequado?", imc_adequado)

# 8 Par ou Impar
numero = int(input("Digite um número inteiro: "))
par = (numero % 2) == 0
print("O número é par?", par)