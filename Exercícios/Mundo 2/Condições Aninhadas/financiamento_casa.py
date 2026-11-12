'Programa para aprovar emprétimos bancários'

print('Digite o valor da casa:')
vl_casa = float(input())
print('Qual o seu salário negote:')
salario = float(input())
print('E em quantos anos você vai pagar a casa:')
ano = int(input())
prestacao = vl_casa (ano * 12)
minimo = salario * 30 / 100
print(f'Para pagar a casa de {vl_casa}R$ em {ano} anos \n a prestação sera de {prestacao}R$')
if prestacao<= minimo:
    print('Concebido')
else:
    print('Não concebido')