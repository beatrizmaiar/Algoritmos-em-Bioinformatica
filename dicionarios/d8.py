"""Crie um programa que gerencia o aproveitamento de um jogador de futebol. o programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols realizados durante o campeonato"""

nome = input('digite seu nome: ')
part = int(input('digite a quantidade de partidas: '))
gols = int(input('digite a quantidade de gols: '))

jogador = {
    "Nome" : nome,
    "Partidas" : part,
    "gols" : gols
}

print(jogador)
