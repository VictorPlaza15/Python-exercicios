
print('Escreva o tamanho da Primeira linha')
l1 = float(input())
print('Escreva o tamanho da Segunda linha')
l2 = float(input())
print('Escreva o tamanho da Terceira e última linha')
l3 = float(input())
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('É possivel')
else:
    print('Não é possivel')
    