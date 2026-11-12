'Programa que leia o ano de nascimento de um atleta e mostra sua categoria'

print('Digite o ano de nascimento do atleta, para descobrir sua cateoria:')
idade = int(input())
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')
