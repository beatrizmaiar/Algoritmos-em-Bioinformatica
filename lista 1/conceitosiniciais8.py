"""Crie um programa que calcule o tempo de viagem, pedindo ao usuário a distância e a velocidade."""

distancia = float(input('digite a distancia da viagem que será realizada: '))
velocidade = float(input('digite a velocidade em que você dirigirá: '))

tempo = distancia/velocidade

print(f'o tempo da viagem é de {tempo} horas')
