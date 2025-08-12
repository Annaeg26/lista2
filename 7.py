'''Faça um Programa que leia três números e mostre o maior e 
o menor deles.'''

n1 = float(input('Digite o primeiro número'))
n2 = float(input('Digite o segundo número'))
n3 = float(input('Digite o terceiro número'))

maior = max(n1,n2,n3) #pega o maior valor
menor = min(n1,n2,n3) #pega o menor valor

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
