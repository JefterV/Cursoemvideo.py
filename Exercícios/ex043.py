altura = float(input('Qual sua altura? m: '))
peso = float(input('Qual é o seu peso? kg: '))
imc = peso / (altura ** 2)
print('O seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso. ')
elif imc >= 18.5 and imc <=25:
    print('Você está no peso ideal.')
elif imc <= 30:
    print('Você está acima do peso.')
elif imc > 30 and imc <=40:
    print('Você está emo Obsidade, tome cuidado...')
else:
    print('Você está muito acima do peso, está em obsidade morbida. Procure um medico, URGENTE!')