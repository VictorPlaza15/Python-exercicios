'Programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o último nome separadamente'

nome = input('Seu nome: ').strip().title()
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))
