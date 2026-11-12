'Professor que quer sortear ordem de apresentação de trabalhos dos alunos'
'Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'

import random
print('Digite o nome quatro de alunos, para a ordem de apresentação!')
apresentacao1 = str(input('Digite o nome do primeiro aluno: '))
apresentacao2 = str(input('Agora, digite o nome do segundo aluno: '))
apresentacao3 = str(input('Digite o nome do terceiro aluno: '))
apresentacao4 = str(input('E por último, digite o nome do quarto aluno: '))
ap = [apresentacao1, apresentacao2, apresentacao3, apresentacao4]
random.shuffle(ap)
print('A ordem de apresentação é: [{}]'.format(ap))