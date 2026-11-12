'Programa que faça uma contagem regressiva de 10 até 0, com 1 segundo de intervalo'

from time import sleep

for count in range(10, 0, -1):
    print(count)
    sleep(1)
print('Decolar!!!')
