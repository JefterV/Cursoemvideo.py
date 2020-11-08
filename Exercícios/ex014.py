c = float (input('Qual a temperatura de onde você está em graus ºC:'))
f = 9 * c / 5 + 32
print ('O valor em graus Cº é {} e em Fº {}'.format(c, f))

f0 =  float (input('Agora nós informe a temperatura em graus Fº:'))
c0 = (f0 - 32) * 5 / 9
print ('De acordo com a sua informação, ai está com {} Fº, convertendo para Cº fica {}'.format(f0, c0))