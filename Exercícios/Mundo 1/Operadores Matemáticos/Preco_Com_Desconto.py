'Faça um algoritmo que lê o preço de um produto e mostre seu preço, com 5% de desconto'

preco = float(input('Digite o preço do produto: '))
valor_do_desconto = preco *(5 / 100) 
valor_final = preco - valor_do_desconto
print('O valor final do produto com 5% de desconto é: R${0}'.format(round(valor_final, 2)))
