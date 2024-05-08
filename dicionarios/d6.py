"""Escreva um programa para verificar se uma chave específica existe no dicionário ou não."""

dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

chave_especifica = "idade"

if chave_especifica in dicionario:
    print(f"A chave '{chave_especifica}' existe no dicionário.")
else:
    print(f"A chave '{chave_especifica}' não existe no dicionário.")

