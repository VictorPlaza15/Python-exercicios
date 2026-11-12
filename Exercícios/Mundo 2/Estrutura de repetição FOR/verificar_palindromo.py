'Programa que leia uma frase qualquer e diga se ela é um palíndromo ou não, desconsiderando os espaços'

print('Digite uma frase')
frase = str(input())
for count in range(len(frase)):
    frase = frase.replace(' ', '')
    frase = frase.lower()
    if frase == frase[::-1]:
        print('A frase é um palíndromo')
        break
    else:
        print('A frase não é um palíndromo')
        break
