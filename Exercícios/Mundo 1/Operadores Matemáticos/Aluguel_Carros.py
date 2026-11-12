'Programa que pergunta a quantidade de Km percorrido por um carro alugado'
'e a quantidade de dias pelos quais ele foi alugado'

nome = input('Escreva seu nome: ')
carro = input('Qual foi o carro alugado: ')
dias = int(input('Certo {0}! quantos dias esse {1}, foi alugado? '.format(nome, carro)))
km_percorrido = float(input('E {0}, qual foi a quilometragem percorrida pelo {1}? Km'.format(nome, carro)))
valor = (dias * 60)+(km_percorrido * 0.15)
print('Então {0}, o carro alugado foi um {1}, o total a pagar vai ser: R${2}'.format(nome. carro, valor))
