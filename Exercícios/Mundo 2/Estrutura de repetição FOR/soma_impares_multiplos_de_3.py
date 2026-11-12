'Programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 a 500'

s = 0
for count in range(1, 501):
    if count % 2 != 0 and count % 3 == 0:
        s += count
print(s)
