"""Crie uma função chamada "maior_palavra" que recebe uma lista de palavras como parâmetro e retorna a maior palavra dessa lista."""

def maior_palavra(*a):
   return max(a)

a = input('digite as palavras que deseja comparar: ')
b = a.split()
print('a maior palavra é: ', maior_palavra(*b))

