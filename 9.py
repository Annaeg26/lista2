'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
a, b, c = sorted([n1,n2,n3])
a, b, c = reversed([a,b,c])

print(a, b,c)