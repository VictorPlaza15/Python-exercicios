'Desenvolver um programa que leia o nome do aluno e as suas duas notas, calcule a média e mostre o resultado.'

aluno = input('Qual seu nome: ')
n1 = float(input('Certo! {} Digite sua primeira nota: '.format(aluno)))
n2 = float(input('{}, agora digite a sua segunda nota: '.format(aluno)))
media = (n1 + n2) / 2
print('{}, sua média é: {:.1f}'.format(aluno, media))