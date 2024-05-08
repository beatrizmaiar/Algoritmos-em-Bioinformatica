"""Escreva um programa para agrupar uma lista de dicionários por uma chave específica"""

# Lista de dicionários de exemplo
lista_de_dicionarios = [
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"},
    {"id": 3, "nome": "José"},
    {"id": 4, "nome": "Ana"},
    {"id": 5, "nome": "Pedro"},
    {"id": 6, "nome": "Carla"},
    {"id": 7, "nome": "Mariana"},
    {"id": 8, "nome": "Paulo"},
    {"id": 9, "nome": "Fernanda"},
    {"id": 10, "nome": "Gabriel"},
]

# Chave específica para agrupamento
chave_especifica = "id"

# Inicializar dicionário para agrupamento
grupos = {}

# Agrupar os dicionários por chave específica
for dicionario in lista_de_dicionarios:
    valor_da_chave = dicionario[chave_especifica]
    if valor_da_chave in grupos:
        grupos[valor_da_chave].append(dicionario)
    else:
        grupos[valor_da_chave] = [dicionario]

# Imprimir os grupos
for valor_da_chave, lista_de_dicionarios in grupos.items():
    print(f"Grupo {valor_da_chave}:")
    for dicionario in lista_de_dicionarios:
        print(dicionario)
    print()

