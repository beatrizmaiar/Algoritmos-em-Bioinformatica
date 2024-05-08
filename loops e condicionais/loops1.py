"""Em química, o pH de uma solução aquosa é uma medida da sua acidez.Os Valores de pH variam entre 0 e 14. Soluções ácidas tem pH maior que 7. Soluções básicas tem pH menor que 7. Soluções neutras tem pH igual a 7. Escreva duas funções que recebem um número correspondente ao pH de uma solução aquosa e exibem na tela o tipo de solução (algo como “A solução é ácida”)."""

ph = int(input('digite o ph: '))

if ph>7:
  print('sua solução é ácida')
elif ph == 7:
  print('sua solução é neutra')
else:
  print('sua solução é básica')
