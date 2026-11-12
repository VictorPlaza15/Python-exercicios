'Programa que leia o nome, idade, sexo de 4 pessoas'

count_idade = 0
i = 0
velho = 0
for count in range (1, 5):
    print('Escreva seu nome: ')
    nome = str(input()).lower()
    print('Agora digite a sua idade: ')
    idade = int(input())
    print('E por fim digite seu sexo: \n - Masculino \n - Feminino')
    sx = str(input()).lower
    count_idade = count_idade + idade
    if count == 1:
        velho = idade
    else:
        if sx == 'masculino' or sx =='m' and velho < idade:
            velho = idade
            nome_do_velho = nome
    if sx == 'feminino' or sx =='f' and idade < 20:
        i =  i + 1
    media = count_idade / 4
print(media, velho, i)
