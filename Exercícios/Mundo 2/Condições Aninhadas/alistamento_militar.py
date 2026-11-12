'Programa que leia o ano de nascimento de um jovem e informe, de acordo com seu ideal com sua idade'

print('Digite quantos anos você tem agora!')
idade = int(input())
if idade < 18:
    tempo = 18 - idade
    print(f'Você ainda tem {idade} anos, faltam {tempo} anos para se alistar!')
elif idade == 18:
    print('Hora de se alistar!!!')
else:
    tempo = idade - 18
    print(f'Você já tem {idade} anos, passou {tempo} anos de se alistar!')
