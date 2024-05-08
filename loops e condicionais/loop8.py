"""Crie um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa e forneça uma classificação com base no resultado."""

peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/(altura**2)

if imc < 18.5:
  print('você está abaixo do peso')
elif imc > 18.5 and imc < 24.9:
  print('você está com o peso ideal')
elif imc>25 and imc<29.9:
  print('voce está com obesidade classe 1')
elif imc>35 and imc<39.9:
  print('voce está com obesidade classe 2')
else:
  print('você está com obesidade mórbida')
