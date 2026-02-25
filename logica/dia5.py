# Estruturas de repetição
# repetir n vezes onde n a gente pode definir, ou é uma condição

frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print("Fruta:", fruta)

#repita até o número 5
# o range cria uma lista, nesse caso de 0 a 4, ou seja, 5 números
for i in range(5):
    print("Número:", i)

# while

contador = 0

while contador < 5:
    print("Contador:", contador)
    #contador para acabar o loop, senão ele vai ficar infinito
    contador += 1

for i in range(10):
    if i == 5:
        break # feito para sair do loop
    print("Número:", i)

for i in range(10):
    if i == 3:
        continue # feito para pular a iteração atual e continuar com a próxima
    print("Número:", i)

# Calcular a multiplicação

n = int(input("Digite um número para calcular a tabuada: "))
multiplicacao = 0
for i in range(1, n+1):
    resultado = n * i
    print(resultado)

# identificar numeros pares e ímpares

pares = 0
impares = 0

for i in range(1, 7+1):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Números pares:", pares)
print("Números ímpares:", impares)

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
print(num_sorteado) # para testar 
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

# Desafios Extras
# 1 Calculando Fatorial de um Número

num_fatorial = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1

for i in range(1, num_fatorial + 1):
    fatorial *= i
print(f"O fatorial de {num_fatorial} é: {fatorial}")

# 2 Série Fibonacci

n = int(input("Digite o número de termos da série Fibonacci: "))

termo1 = 0
termo2 = 1
contador = 0

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
elif n == 1:
    print("Série Fibonacci:", termo1)
else:
    print("Série Fibonacci")
    while contador < n:
        print(termo1)
        prox_termo = termo1 + termo2
        termo1 = termo2
        termo2 = prox_termo
        contador += 1

#3 Jogoda Forca Simples

palavra_secreta = "python"
letras_adivinhadas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and "_" in letras_adivinhadas:
    print("Palavra:", " ".join(letras_adivinhadas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_adivinhadas[i] = letra
    else:
        tentativas -= 1
        print(f"Letra incorreta! Tentativas restantes: {tentativas}")

if "_" not in letras_adivinhadas:
    print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("Game Over! A palavra secreta era:", palavra_secreta)
