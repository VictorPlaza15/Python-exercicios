'Programa que leia um número inteiro e diga se ele é ou não um número primo'

print('Digite um número e veja se é primo ou não:')
num = int(input())
for count in range(2, num):
    if num % count == 0:
        print('O número {} não é primo'.format(num))
        break
else:
    print('O número {} é primo'.format(num))
