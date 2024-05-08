"""Crie uma função na qual calcula o valor do seno a partir da série de Taylor (50 primeiros termos) e cosseno a partir da seguinte identidade a baixo. Obs: Fazer a serie utilizando for e utilizar a função fatorial desenvolvida no exercício 1."""

def fat(a):
  if(a>1):
    return a*fat(a-1)
  else:
    return 1


def seno(x):
    result = 0
    for n in range(50):
        termo = ((-1) ** n) * (x ** (2 * n + 1)) / fat(2 * n + 1)
        result += termo
    return result

def cosseno(x):
    result = 0
    for n in range(50):
        termo = ((-1) ** n) * (x ** (2 * n)) / fat(2 * n)
        result += termo
    return result

# Exemplo de uso:
angulo = float(input("Digite o valor do ângulo em radianos: "))
print("Seno:", seno(angulo))
print("Cosseno:", cosseno(angulo))

