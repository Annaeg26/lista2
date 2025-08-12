'''Faça um Programa que verifique se uma letra digitada é 
vogal ou consoante.'''

letra=input('uma letra').lower()
if letra in 'aeiou':
    print('foi digitado uma vogal')
else:
    print('fo digitado uma consoante')