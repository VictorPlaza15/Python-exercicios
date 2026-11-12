'Programa que leia três números e fala qual é maior e qual é menor'

print('Digite um número:')
num1 = float(input())
print('Digite outro número:')
num2 = float(input())
print('Digite mais um número:')
num3 = float(input())
print('O maior número é:', max(num1, num2, num3))
print('O menor número é:', min(num1, num2, num3))
