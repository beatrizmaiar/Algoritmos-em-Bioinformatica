"""Faça um programa que leia o nome RA e média final de uma aluno. Armazene todas as informações num dicionário. No final programa deve imprimir as informações do dicionário e situação do aluno (reprovado, exame ou aprovado). Utilize as regras da UNIFESP para definir a situação do aluno."""

nome = input('digite seu nome: ')
ra = int(input('digite seu ra: '))
mf = float(input('digite sua media final: '))

aluno = {
    "Nome": nome,
    "RA": ra,
    "Média Final": mf
}

if mf < 3:
  aluno["situação"] = "reprovado"
elif mf > 3 and mf < 6:
  aluno["situação"] = "exame"
else:
  aluno["situação"] = "aprovado"

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

