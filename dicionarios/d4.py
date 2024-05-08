"""Crie um programa que leia nome, sexo, peso e altura de várias pessoas. guarde os dados de cada pessoa num dicionário individual e acrescente o IMC da pessoa. Organize todos os dicionários em uma lista. No final mostre a. Quantas pessoas foram cadastradas b. Qual é o peso médio das pessoas c. Qual é a altura média das pessoas d. Qual é IMC médio das pessoas"""

# Inicializando a lista de pessoas
pessoas = []

# Variáveis para cálculo do peso médio, altura média e IMC médio
soma_peso = 0
soma_altura = 0
soma_imc = 0

# Solicitar entrada do usuário para cada pessoa
quantidade = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(quantidade):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ")
    peso = float(input(f"Digite o peso da pessoa {i+1} em kg: "))
    altura = float(input(f"Digite a altura da pessoa {i+1} em metros: "))

    # Calculando o IMC
    imc = peso / (altura ** 2)

    # Criando o dicionário com os dados da pessoa
    pessoa = {
        "Nome": nome,
        "Sexo": sexo,
        "Peso": peso,
        "Altura": altura,
        "IMC": imc
    }

    # Adicionando o dicionário à lista de pessoas
    pessoas.append(pessoa)

    # Atualizando as variáveis para cálculo das médias
    soma_peso += peso
    soma_altura += altura
    soma_imc += imc

# Calculando as médias
quantidade_pessoas = len(pessoas)
peso_medio = soma_peso / quantidade_pessoas
altura_medio = soma_altura / quantidade_pessoas
imc_medio = soma_imc / quantidade_pessoas

# Mostrando os resultados
print("\nResultados:")
print(f"a. Quantidade de pessoas cadastradas: {quantidade_pessoas}")
print(f"b. Peso médio das pessoas: {peso_medio:.2f} kg")
print(f"c. Altura média das pessoas: {altura_medio:.2f} metros")
print(f"d. IMC médio das pessoas: {imc_medio:.2f}")

