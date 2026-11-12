'Sortear um dos seus quatro alunos para apagar o quadro.'
'Faça um programa que leia o nome deles e escrevendo o nome do escolhido'

import random

print('Digite o nome quatro de alunos!')
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Agora, digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('E por último, digite o nome do quarto aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolher = random.choice(alunos)
print('O aluno escolhido para apagar o quadro é: ', escolher)
