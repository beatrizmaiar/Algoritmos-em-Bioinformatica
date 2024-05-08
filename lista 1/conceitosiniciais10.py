"""A resistência combinada de três resistores R1, R2 e R3 em
paralelo é dada por FÓRMULA Crie três variáveis com três valores de resistências e calcule a
resistência resultante."""

var1 = int(input('digite a variavel 1: '))
var2 = int(input('digite a variavel 2: '))
var3 = int(input('digite a variavel 3: '))

r= (1/((1/var1)+(1/var2)+(1/var3)))

print(f'a resistencia é de {r:.2f}')
