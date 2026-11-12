'Faça um programa que leia seis números inteiros e mostre a soma apenas daquelas que foram pares. Se o valor digitado for ímpar, desconsidere-o'

soma = 0
for count in range(1, 7):
    print('Digite um número inteiro:')
    num = int(input())
    if num % 2 == 0:
        soma += count
    else:
        print('Ímpar não consideramos')
print(soma)
