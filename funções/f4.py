"""Crie uma função chamada "calculadora" que recebe três parâmetros: dois números e uma operação matemática (+, -, *, /). A função deve retornar o resultado da operação."""

def calculadora(a,b,p):
  if p == '+':
    return a+b
  elif p == '-':
    return a-b
  elif p == '*':
    return a*b
  elif p == '/':
    return a/b
  else:
    print('operação não aceita')

a= int(input('digite o numero a: '))
b = int(input('digite o numero b: '))
p = input('qual operação você quer realizar: ')
print(calculadora(a,b,p))

