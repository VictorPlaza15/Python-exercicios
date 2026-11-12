'Programa que faz o computador pensar em um número inteiro de 0 a 5 e peça para o usuário descobrir qual foi número escolhido'

import random

num = [0, 1, 2, 3, 4, 5]
num_pensado = random.choice(num)
print('Advinhe o número que estou pensando: ')
tentativa = int(input())
if tentativa == num_pensado:
    print('PARABÉNS!!!')
else:
    print('PERDEU! eu pensei no número {}!!'.format(num_pensado))
