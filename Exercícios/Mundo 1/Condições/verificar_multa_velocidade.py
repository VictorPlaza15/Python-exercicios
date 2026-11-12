'Programa que lê a velocidade do carro'


print('Qual foi a velocidade do veículo, em Km/h: ')
velocidade = int(input())
if velocidade > 80:
    print('Você foi multado!!!')
    multa = (velocidade - 80) * 7.00 
    print('Sua multa foi de {}R$'.format(multa))
else:
    print('Você não foi multado, continue dirigindo com segurança!')