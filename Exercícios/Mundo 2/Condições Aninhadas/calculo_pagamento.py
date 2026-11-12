'Programa que calcule o valor a ser pago por um produto, preço normal e condição de pagamento'

print('Qual o produto a ser pago?')
fds_esse_aq = str(input())
print('Qual o valor do produto')
vl = float(input())
print('Digite o número com base na forma de pagamento? \n1° À vista no Dinheiro ou Cheque \n2° á vista no Cartão \n3° Em até 2x no cartão \n4° Em até 3x ou mais no cartão')
pagamento = input()
if pagamento == '1':
    vl_final = vl - (vl * 10/100)
    print(f'O valor fica em torno de: {vl_final}R$')
elif pagamento == '2':
    vl_final= vl - (vl * 5/100)
    print(f'O valor fica em torno de: {vl_final}R$')
elif pagamento == '3':
    parcela = vl / 2
    print(f'O valor fica em torno de: {vl}R$ \n Com cada parcela de {parcela}R$')
else:
    print('Quantas parcelas?')
    mes = int(input())
    juros = vl * 0.20 * mes
    vl_final = vl + (vl * 0.20)
    parcela = vl_final / mes
    print(f'Então vai ficar em torno de: {vl_final}R$ \nSendo parcelado em até {mes}x de {parcela}R$')
