'Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, e tangente desse ângulo'
from math import cos, tan, sin, radians, ceil

angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('{0} {1} {2}'.format(round(seno, 3), round(cosseno, 3), round(tangente, 3)))
