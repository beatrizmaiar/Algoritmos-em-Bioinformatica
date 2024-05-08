"""Escreva um script que leia a quantidade de dias,horas, minutos e segundos para o usuário. Calcule o total em segundos."""

dias = int(input('digite a quantidade de dias:'))
horas = int(input('digite a quantidade de horas:'))
minutos = int(input('digite a quantidade de minutos:'))
segundos = int(input('digite a quantidade de segundos:'))

segundos = segundos + minutos*60 + horas*60*60 + dias*24*60*60

print(f'a quantidade em segundos do período inserido é igual a {segundos}')
