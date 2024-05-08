"""Escreva uma função em Python que receba uma string como entrada e retorne a string com cada palavra em ordem in"""

string = input('digite uma palavra: ')
a= len(string)
inverso = ""
for i in range(a-1,-1,-1):
  inverso = inverso + string[i]

print(inverso)
