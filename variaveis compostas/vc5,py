"""Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0"""

medias = []

for i in range(5):
    notas = input("Informe as 4 notas: ")

    notas = [float(nota) for nota in notas.split()]

    media = sum(notas)/4
    medias.append(media)

aprovados = sum(1 for media in medias if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {aprovados}")

