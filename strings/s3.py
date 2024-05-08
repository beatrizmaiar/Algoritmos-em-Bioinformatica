"""Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string. String: TTAAC Resultado: T: 2x A: 2x C: 1x"""

string = input('digite uma string: ')
a = set(string)

for i in a:
  print(i,':', string.count(i),'x')



