"""Faça um Programa que leia 20 números inteiros e armazene-os num lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima os três vetores."""

numeros = []

for i in range(20):
  num = int(input('digite o numero: '))
  numeros.append(num)

par = [num for num in numeros if num%2 == 0]
impar = [num for num in numeros if num%2 == 1]

print(par)
print(impar)
