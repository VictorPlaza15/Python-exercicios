'Programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores'

c = 0
a = 0
i = 0
for count in range(0, 7):
    print('Digite qual ano você nasceu')
    ano = int(input())
    if ano > 2026:
        print('Volta pro seu tempo seu viado \n')
        i+= 1
    elif ano <= 2008:
        print('Você já é maior de idade \n')
        a+= 1
    else:
        print('Você é menor de idade ainda \n')
        c+= 1
print(f'O número de pessoas menores de idade é: {c} \nO número de pessoas maiores de idade é: {a} \nO número de pessoas que não são desse ano é: {i}')
