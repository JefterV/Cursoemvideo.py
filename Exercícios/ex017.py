import math
hp= float (input('Digite um cateto oposto:'))
hp0= float (input ('Digite o cateto adjacente:'))
hp1= math.hypot(hp, hp0)
print ('A hipotenusa desse triangulo é {:.2f}'.format(hp1)) 

print ('')
co= float (input ('Digite o valor do cateto oposto:'))
ca= float (input('Digite o valor do cateto adjacente:'))
cao= (co ** 2 + ca ** 2) ** (1/2)
print ('O valor da hipotenusa é {:.2f}'.format(cao))