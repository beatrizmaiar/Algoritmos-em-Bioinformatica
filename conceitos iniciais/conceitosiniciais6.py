"""Escreva um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa."""

peso = float(input('digite seu peso:'))
altura = float(input('digite sua altura:'))

imc = peso/altura**2

print(f'seu imc é igual a {imc:.2f}')


