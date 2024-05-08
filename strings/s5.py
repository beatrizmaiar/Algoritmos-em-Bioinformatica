"""Escreva uma função em Python que receba uma string como entrada e verifique se ela é um palíndromo."""

string = input('digite uma palavra: ')
a= len(string)
palindromo = ""

for i in range(a-1,-1,-1):
  palindromo = palindromo + string[i]

if string == palindromo:
  print('é palindromo')
else:
  print('não é palindromo')
