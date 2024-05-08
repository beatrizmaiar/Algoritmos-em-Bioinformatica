"""Implemente uma função chamada "soma_recursiva" que recebe um número inteiro positivo como parâmetro e retorna a soma de todos os números inteiros de 1 até esse número, utilizando recursividade."""

def soma_recursiva(a):
  if a != 1:
    return a + soma_recursiva(a-1)
  else:
    return 1

a = int(input('digite um numero: '))
print(soma_recursiva(a))
