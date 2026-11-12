'Programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão'

print('Digite o primeiro termo do PA:')
termo = int(input())
print('Digite a razão do PA:')
razao = int(input())
for count in range(termo, termo + 10 * razao, razao):
    print('O termo é:', count)
