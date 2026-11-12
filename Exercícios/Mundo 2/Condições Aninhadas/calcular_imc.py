'Lógica que leia o peso e a altura  de uma pessoa, calcule seu IMC e mostra seu status'

print('Digite o seu peso')
peso = float(input())
print('Digite a sua altura')
altura = float(input())
imc = (altura**2) / peso
if imc < 18.5:
    print('Está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Está no peso ideal')
elif imc > 25 and imc <= 30:
    print('Está acima do peso')
elif imc > 30 and imc <= 40:
    print('Está obeso já! vai para queimar caloria!')
else:
    print('Quilos mortais?!')

