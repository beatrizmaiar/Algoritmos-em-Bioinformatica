"""Crie um script em Python que solicite o nome, altura e peso de uma pessoa e mostre a seguinte mensagem: “João tem 90 kilos e altura de 1.78 e portanto o IMC é de 28.4”."""

nome = input('Digite o seu nome:')
altura = float(input('digite sua altura:'))
peso = int(input('Digite seu peso:'))

IMC = peso/altura**2

print(f'{nome} tem {peso} kilos e altura de {altura} e portanto o IMC é de {IMC}')
