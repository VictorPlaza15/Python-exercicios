'Refaze o desafio número 9 da tabuada, com o laço, e com o número do usuário'

n_inicial = int(input('Digite um numero inteiro: '))
for num in range(1, 11):
    resultado = n_inicial * num
    print('{0} X {1} = {2}'.format(n_inicial, num, resultado))