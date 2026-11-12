'Programa que leia o nome de uma pessoa e diga se ela tem silva no nome'

nome = input('Nome: ').strip().title()
print('A pessoa tem "Silva" no nome: {}'.format('Silva' in nome))