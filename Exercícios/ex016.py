from math import trunc, sqrt
n= float (input('Digite um numero'))
corte= trunc (n)
print ('A perte inteira de {} é {}'.format(n, corte))
print ('')

raiz= float (input('Calcule a raiz quadrada de:'))
rz0= sqrt (raiz)
print ('A raiz quadrada de {} é {}'.format(raiz, rz0))
print ('A raiz quadrada sem numeros quebrados é {}'.format( trunc(rz0)))