"""Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida. Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}"""

frase = input("Digite uma frase: ")
# Inicializa um dicionário vazio para armazenar contagens
contagem = {}
# Percorre cada caractere na frase
for i in frase:
    # Verifica se o caractere já está no dicionário
    if i in contagem:
        # Se estiver, incrementa o valor correspondente à chave
        contagem[i] += 1
    else:
        # Se não estiver, adiciona a chave ao dicionário com valor 1
        contagem[i] = 1
# Imprime o dicionário resultante
print(contagem)

