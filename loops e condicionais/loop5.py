"""Escreva um programa que encontre e imprima todos os números primos entre 1 e 100."""

limite = 100

for num in range(2, limite + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)



