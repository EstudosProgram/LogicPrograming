# Estruturas de repetição
# repetir n vezes onde n a gente pode definir, ou é uma condição

# frutas = ['maçã', 'banana', 'laranja']

# for fruta in frutas:
#     print("Fruta:", fruta)

# #repita até o número 5
# # o range cria uma lista, nesse caso de 0 a 4, ou seja, 5 números
# for i in range(5):
#     print("Número:", i)

# # while

# contador = 0

# while contador < 5:
#     print("Contador:", contador)
#     #contador para acabar o loop, senão ele vai ficar infinito
#     contador += 1

# for i in range(10):
#     if i == 5:
#         break # feito para sair do loop
#     print("Número:", i)

# for i in range(10):
#     if i == 3:
#         continue # feito para pular a iteração atual e continuar com a próxima
#     print("Número:", i)

# # Calcular a multiplicação

# n = int(input("Digite um número para calcular a tabuada: "))
# multiplicacao = 0
# for i in range(1, n+1):
#     resultado = n * i
#     print(resultado)

# # identificar numeros pares e ímpares

# pares = 0
# impares = 0

# for i in range(1, 7+1):
#     if i % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# print("Números pares:", pares)
# print("Números ímpares:", impares)

# Exercícios Práticos

# 1 Imprimindo Números de 1 a 10

for i in range(1, 11):
    print(i)

# 2 Calculando a Soma dos Números de 1 a N

n = int(input("Digite um número inteiro positivo para a soma: "))
soma = 0
for i in range(1, n+1):
    soma += i # soma = soma + i
print("A soma dos números de 1 a", n, "é:", soma)

# 3 Tabuada de um Número

num = int(input("Digite um número para calcular a tabuada: "))

for i in range(1, 11):
    resultado = i * num
    print(f"{num} x {i} = {resultado}")

# 4 Contando Números Pares e Ímpares

pares = 0
impares = 0

for i in range(1, 21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números pares:", pares)
print("Números ímpares:", impares)

# 5 Adivinhe o Número
import random

num_sorteado = random.randint(1, 100)
tentativas = 0

while True:
    num_user = int(input("Adivinhe o número entre 1 e 100: "))
    tentativas += 1

    if num_user == num_sorteado:
        print(f"Parabéns! Você acertou o número com {tentativas} tentativas!")
        break
    elif num_user < num_sorteado:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")