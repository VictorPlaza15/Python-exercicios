'Programa que faça o teorema de Pitágroras'
from math import pow, sqrt

comprimento_co = float(input('Digite o comprimento do cateto oposto: '))
comprimento_ca = float(input('Agora, digite o comprimento do cateto adjacente: '))
h = pow(comprimento_co, 2) + pow(comprimento_ca, 2)
print('O comprimento do cateto oposto {0}, o comprimento do cateto adjacente {1}, sua hipotenusa resulta em: {2}'.format(comprimento_co, comprimento_ca, sqrt(round(h, 3))))
