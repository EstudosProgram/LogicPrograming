# Lista de Convidados
lista_festa = ["Milena", "Maria", "João", "Pedro", "Ana", "Lucas"]

for nome in lista_festa:
    print(f"Olá {nome}, você está convidado para a festa!")

# Estatísticas de Números

entrada = input("Digite uma lista de números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

maior_num = max(numeros)
menor_num = min(numeros)
soma = sum(numeros)
media = sum(numeros) / len(numeros)

print(f"Maior número: {maior_num}")
print(f"Menor número: {menor_num}")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media:.2f}")

# Contagem de Caracteres em uma String

frase = input("Digite uma frase: ")
letras = {}

for caractere in frase:
    if caractere.isalpha():  # Contar apenas letras
        caractere = caractere.lower()  # Ignorar maiúsculas/minúsculas
        if caractere in letras:
            letras[caractere] += 1
        else:
            letras[caractere] = 1

for letra, contagem in letras.items():
    print(f"A letra '{letra}' aparece {contagem} vez(es).")

# Ordenando uma Lista

entr = input("Digite uma lista de números separados por espaço: ")
num = [float(num1) for num1 in entr.split()]

num_crescente = sorted(num)
print("Números em ordem crescente:", num_crescente)
num_decrescente = sorted(num, reverse=True)
print("Números em ordem decrescente:", num_decrescente)

# Trabalhando com Tuplas

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

user = int(input("Digite um número de 1 a 12 para obter o mês correspondente: "))

for i in range(len(meses)):
    if user == i + 1:
        print("O mês correspondente é:", meses[i])

# Desafios Extras
