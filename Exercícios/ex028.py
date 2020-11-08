from random import randint
from time import sleep
print('Vou pensar em um numero entre 0 e 5. TENTE ADVINHAR...')
num0= int ( input ('Digite um numero: '))
num1= randint(0,5)
print('PROCESSANDO...')
sleep(3)
if num0 == num1:
    print('PARABÉNS, VOCÊ GANHOU')
else:
    print ('GANHEI, o numero era {}'.format(num1))


