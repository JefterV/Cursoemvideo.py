viagem = float(input('Quantos KM tem sua viagem? '))
num0 = viagem * 0.50
num1 = viagem * 0.45
if viagem >= 200:
    print ('O valor da sua viagem é R${:.2f}'.format(num1))
else:
    print('O valor da sua viagem é R${:.2f}'.format(num0))