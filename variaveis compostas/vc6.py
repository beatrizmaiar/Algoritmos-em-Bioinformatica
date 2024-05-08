"""Escreva uma rotina que recebe uma lista de números e retorna a soma dos quadrados dos números."""

nums = int(input('informe os numeros: '))
nums = [int(i) for i in nums.split()]
soma = sum(i**2 for nums in nums)
print(soma)

