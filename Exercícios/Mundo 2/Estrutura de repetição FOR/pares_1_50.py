'Programa que mostre os números pares entre 1 e 50'

print('Os números pare entre 1 e 50 são:')
for count in range(1, 51):
    if count % 2 == 0:
        print(count)
