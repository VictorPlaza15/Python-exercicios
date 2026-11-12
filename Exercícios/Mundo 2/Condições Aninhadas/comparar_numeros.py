'Programa que leia dois números inteiros e compare-os'

print('Digite o primeiro número:')
num1 = int(input())
print('Digite o segundo número')
num2 = int(input())
if num1 > num2:
    print(f'O número 1 "{num1}" é maior que o número 2 "{num2}"')
elif num1 < num2:
    print(f'O número 2 "{num2}" é maior que o número 1 "{num1}"')
else:
    print('Os números são iguais!')
    