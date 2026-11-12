'Refazer o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sera formado'


print('Escreva o tamanho da Primeira linha')
l1 = float(input())
print('Escreva o tamanho da Segunda linha')
l2 = float(input())
print('Escreva o tamanho da Terceira e última linha')
l3 = float(input())
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    if l1 == l2 and l2 == l3:
        print('Seu triângulo é Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Seu triângulo é Isósceles')
    else:
        print('Seu triângulo é Escaleno')
    print('É possivel')
else:
    print('Não é possivel')
