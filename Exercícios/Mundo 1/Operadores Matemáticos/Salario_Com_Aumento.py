'Algoritmo que lê o salário de um funcionário e mostre seu novo salário, com 15% de aumento'

funcionario = input('Digite seu nome funcionário: ')
salario = float(input('Digite seu salário {}: '.format(funcionario)))
valor_aumento = salario * (15 / 100)
novo_salario = salario + valor_aumento
print('{0}, seu novo salário foi reajustado, e apartir de agora seu salário é de: R${1}' .format(funcionario, round(novo_salario, 2)))
