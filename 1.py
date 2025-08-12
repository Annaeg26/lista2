'''Faça um Programa que peça dois números e imprima o maior deles'''

n1=float(input('Digite o primeiro número'))
n2=float(input('Digite o segundo número'))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
else:
    print(f'{n2} é maior que {n1}')