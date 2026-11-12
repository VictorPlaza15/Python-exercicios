'Programa que lê a largura e a altura de uma parede em metros,'
'calcule a sua área e quantidade de tinta necessária para pinta-lá,'
'sabendo que cada litro de tinta pinta uma área de 2m²'

largura = float(input('Digite a largura da parede: '))
altura = float(input('Agora digite a altura da parede: '))
area = largura * altura
tinta_necessaria = area / 2
print('A área da parede é {0}m² , e você irá precisar de {1} litros de tinta'.format(area, tinta_necessaria))
