"""Escreva um programa que simule um caixa eletrônico, solicitando ao usuário que insira o valor do saque e informando quantas notas de cada valor serão entregues (considere notas de R 100,R  50, R 20,R  10, R 5eR  2)."""

saque = int(input('Digite o valor a ser sacado: '))

resto = saque

n100 = saque//100
resto = saque%100

n50 = resto//50
resto = resto%50

n20 = resto//20
resto = resto%20

n10 = resto//10
resto = resto%10

n5 = resto//5
resto = resto%5

n2 = resto//2
resto = resto%2

print(f'temos {n100} notas de 100, {n50} notas de 50, {n20} notas de 20, {n10} notas de 10, {n5} notas de 5 e {n2} notas de 2')

