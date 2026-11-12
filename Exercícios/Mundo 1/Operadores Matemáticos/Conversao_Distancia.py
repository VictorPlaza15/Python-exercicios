'Escrever um programa que leia uma distância em metros e apresente-a convertida em centímetros e milímetros.'

n_metro = int(input('Digite a distância em metros: '))
cm = n_metro * 100
mm = n_metro * 1000
print('A quantidade de metros são: {0}m\nEm centímetros é: {1}cm \nE em Milímetros é: {2}mm' .format(n_metro, cm, mm))