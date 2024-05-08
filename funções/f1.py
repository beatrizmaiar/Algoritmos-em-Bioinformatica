"""Escreva uma função chamada fatorial para calcular o fatorial de um número inteiro."""

def fat(a):
  if(a>1):
    return a*fat(a-1)
  else:
    return 1

a = int(input('digite um número:'))
print('o seu fatorial é' ,fat(a))
