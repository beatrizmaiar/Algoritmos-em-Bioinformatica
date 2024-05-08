"""Faça um Programa que leia uma lista de 10 números reais e mostre- os na ordem inversa."""

numeros = []

# Solicitar 10 números e armazená-los na lista numeros
for i in range(10):
    numero = float(input("Digite o número real: "))
    numeros.append(numero)

# Exibir os números na ordem inversa
for j in reversed(numeros):
    print(j)

