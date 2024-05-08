"""Escreva um script que pergunte a quantidade de km percorridos por um carro alugado pelo usuário e a quantidade de dias pelo qual o carro foi alugado. Calcule o preço a pagar sabendo que o carro custa 60 reais por dia e 15 centavos por Km rodado."""

km = int(input('quantos km você rodou?'))
dias = int(input('por quantos dias você alugou?'))

aluguel = km*0.15 + 60*dias

print(f'o valor do aluguel é igual a {aluguel}')
