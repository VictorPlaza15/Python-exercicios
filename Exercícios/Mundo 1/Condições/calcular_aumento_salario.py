'Programa que pergunteo salário de um funcionário e calcule o valor do seu aumento'

import math
print('Digite seu salário mensal:')
salario = float(input())
if salario > 1250.00:
    aumento = salario *(10/100)
    vl_final = aumento + salario
    print('Você teve um aumento de 10%! Seu salário agora é de: {}R$'.format(vl_final))
else:
    aumento = salario*(15/100)
    vl_final = aumento + salario
    print('Você teve um aumento de 15%! Seu salário é de: {}R$'.format(vl_final))
