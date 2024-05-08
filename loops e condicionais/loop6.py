"""Escreva um programa que determine se um número é primo ou não."""

num = int(input('digite um número: '))

is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print('não é primo!')
        break
    if is_prime:
        print('é primo!')

