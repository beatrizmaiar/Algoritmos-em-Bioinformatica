"""Faça um script que calcule o aumento de salário. Ele deve solicitar o valor do salário e a porcentagem de aumento. Exiba o valor do aumento e do novo salário."""

salario = float(input('digite o seu salário:'))
aumento = float(input('digite o seu aumento:'))

novosalario = salario*aumento +salario

print(f'o novo salário é {novosalario}')
