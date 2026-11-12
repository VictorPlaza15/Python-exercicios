'Programa que pergunta a distância da viagem em Km. Calcula o preço da passagem.'

print('Digite a distância da viagem percorrida em Km:')
viagem = int(input())
if viagem <= 200:
    passagem = viagem * 0.50
else:
    passagem = viagem * 0.45
print('Sua passagem é de {}R$'.format(passagem))