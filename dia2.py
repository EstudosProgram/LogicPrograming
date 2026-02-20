# Variáveis - lugares que armazenamos dados
idade = 20
nome = "Milena"
altura = 1.58

print(idade)
print(nome)
print(altura)

# Tipos de dados
# int, float, textos = str, bool = true ou false
cidade = 'São Paulo'
print(cidade)

# booleano pode usar para validar se um usuário está logado ou não
esta_logado = True
print(esta_logado)

# verificar o tipo de dado
print(type(nome)) # str -> String
print(type(idade)) # int -> Integer
print(type(altura)) # float -> número com casas decimais
print(type(esta_logado)) # bool -> booleano, só tem dois valores: True ou False

# Operadores
print(5 + 2.1) # soma, resultado é 7.1
print(10 - 3) # subtração, resultado é 7
print(4 * 2) # multiplicação, resultado é 8
print(2 ** 2) # potência, resultado é 4
print(10 / 2) # divisão normal, resultado é um float
print(10 // 2) # divisão inteira, resultado é um int
print(10 % 3) # resto da divisão, resultado é 1

# Concatenação de strings - união de textos
# Unir com o simbolo de +
frase = "Olá "+ nome + " tudo bem?"
print(frase)

# Comparacões com True ou False
maior = 15 > 2
print(maior)
menor = 11 < 10
print(menor)
print(5 == 5) # comparação de igualdade, resultado é True
print(5 != 3) # comparação de desigualdade, resultado é True
print("Milena" == "milena")

# jeito de colocar uma variavel dentro de um texto
num = 10
print("Número:",num)

# Exercicios

# 1 - Declarando variaveis
nome = 'Milena'
idade = 29
altura = 1.60
estudante = True

# 2 - Exibindo as informações
print("Nome:",nome)
print("Idade:",idade)
print("Altura:",altura)
print("Estudante:",estudante)

# 3 - Operações simples
idade = 37
ano_nascimento = 2026 - idade
print("Ano de nascimento:", ano_nascimento)

# 4 - Manipulação de strings
nome_cachorro = "Jade"
idade_cachorro = 6
idade_humana = idade_cachorro * 7
print("A idade do(a) " + nome_cachorro + " em anos humanos é:",idade_humana)

# 5 - Calculadora simples
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
print("A soma é:",soma)
print("A subtração é:",subtracao)
print("A multiplicação é:",multiplicacao)
print("A divisão é:",divisao)

# 6 - Conversor de temperaturas
celcius = float(input("Digite a temperatura em Celcius: "))
fahrenheit = (celcius * 9/5) + 32
print("A temperatura em Fahrenheit é:",fahrenheit)

# 7 - Calculando a área de um círculo
raio = float(input("Digite a área do círculo: "))
area = 3.14159 * raio ** 2
print("A área do círculo é:",area)