'Programa que leia o peso de cinco pessoas. No final, mostra qual foi o maior e o menor peso lidos'

peso_menor = 0
peso_maior = 0
for count in range(1, 6):
    print(f'Digite seu peso pessoa N°: {count}')
    peso = float(input())
    if peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso
print(f'Maior peso é: {peso_maior}\nMenor peso é: {peso_menor}') 
