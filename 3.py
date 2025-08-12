'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - 
Masculino, Sexo Inválido.'''

letra=input('Digite F - Feminino ou M - Masculino').lower()
if letra == 'f':
    print('Gênero Feminino')
elif letra == 'm':
    print('Gênero Masculino')
else:
    print('Inválido')
