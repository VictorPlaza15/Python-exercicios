'programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão: binário, Octal, Hexadecimal'

print('Digite um número inteiro:')
num = int(input())
print('Agora escolha algumas das opções de conversão \n1° Binário \n2° Octal \n3° Hexadecimal')
opc = int(input())
if opc == 1:
    num_bin = bin(num)
    print(f'O número {num} em binário é: {num_bin[2:]}')
elif opc == 2:
    num_oct = oct(num)
    print(f'O número {num}, em octal é: {num_oct[2:]}')
elif opc == 3:
    num_hex = hex(num)
    print(f'O número {num}, em hexadecimal: {num_hex[2:]}')
else: 
    print('O número escolhido não está na lista! tente outro número')
