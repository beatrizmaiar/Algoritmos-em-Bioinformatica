#Crie um programa que imprima a sequência de Fibonacci até o décimo termo usando um loop for.

i = 0
j = 1
k = 0

for _ in range(10):
    print(k)
    i, j = j, i + j
    k = i

