velocidade = int(input('Seu carro estava em qual velociade? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print ('MULTADO! Você exedeu o limite liberado, que é 80km/h.\n Você terá que pagar R${}\n Dirija com cuidado.'.format(multa))
else:
    print('Parabéns você está no limite, dirija com cuidado.')