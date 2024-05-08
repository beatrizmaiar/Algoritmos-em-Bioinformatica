""" Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo."""

from re import T
def mult(a,b):
  if b%a==0:
    return True
  else:
    return False

a= int(input('digite o numero a: '))
b = int(input('digite o numero b: '))
print(mult(a,b))
