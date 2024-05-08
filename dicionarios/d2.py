"""Crie um dicionário, chamado frutas, de frutas e seus preços. a. Crie um segundo dicionário chamado compras na qual as chaves são as frutas e valores é a quantidade a ser comprada b. Calcule o preço total de um carrinho de compras de frutas usando o dicionário criado no exercício anterior. c. Remova todas as frutas do dicionário de frutas que custam mais de R$ 5,00."""

frutas = {"maçã": 2.50,
    "banana": 3.00,
    "laranja": 4.50,
    "uva": 6.00,
    "abacaxi": 7.50
          }

compras = {"maçã": 3,
    "banana": 2,
    "uva": 1}

preco_total = 0

for fruta, quantidade in compras.items():
    # Verificar se a fruta está no dicionário de preços
    if fruta in frutas:
        # Adicionar o preço da fruta multiplicado pela quantidade à soma total
        preco_total += frutas[fruta] * quantidade

print("Preço total do carrinho de compras:", preco_total)

# Remover frutas do dicionário que custam mais de R$ 5,00
frutas_a_remover = [fruta for fruta, preco in frutas.items() if preco > 5.00]

# Remover as frutas do dicionário de frutas
for fruta in frutas_a_remover:
    del frutas[fruta]

print("Dicionário de frutas após remoção:", frutas)
