"""Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas. 1a string: AAACTBF 2a string: CBT"""

string1 = input('digite a primeira string: ')
string2 = input('digite a segunda string: ')

set1 = set(string1)
set2 = set(string2)

caracteres_comuns = set1.intersection(set2)

print(''.join(caracteres_comuns))

