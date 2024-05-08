"""Crie um programa que determine se um número é um número de Armstrong ou não. Um número de Armstrong é aquele que é igual à soma de seus dígitos elevados à potência do número de dígitos."""

num = int(input("Digite um número: "))

num_digitos = len(str(num))

soma = 0
temp = num
while temp > 0:
    digito = temp % 10
    soma += digito ** num_digitos
    temp //= 10

if num == soma:
    print(num, "é um número de Armstrong.")
else:
    print(num, "não é um número de Armstrong.")

