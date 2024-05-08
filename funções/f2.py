"""Escreva uma função chamada maxnum que retorne o maior número de um conjunto de números. Utilize empacotamento para fazer a função."""

def maxnum(*a):
  return max(a)

a = list(input('digite varios numero: '))
print('o numero maximo é', maxnum(*a))
