'Algoritmo que converte graus Celsius para graus Fahrenheit'

temp = float(input('Digite a temperatura em Graus Celsius: '))
fahrenheit = (temp * 1.8) + 32
print('A temperatura em graus Celsius é °C{0}, e para a temperatura fahrenheit é: °F{1}'.format(temp, round(fahrenheit, 2)))
