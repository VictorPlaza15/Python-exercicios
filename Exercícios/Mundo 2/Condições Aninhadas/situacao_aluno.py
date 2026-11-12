'Programa que leia duas notas de aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média'

print('Digite a primeira nota do seu boletim:')
nota1 = float(input())
print('Digite a segunda nota do boletim:')
nota2 = float(input())
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO!!!')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÂO!!')
else:
    print('APROVADO!')
