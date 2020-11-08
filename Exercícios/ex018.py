from math import radians, sin, cos, tan
va= float (input('Digite o grau:'))
seno= sin(radians(va))
print ('O seno de {:.2f} é igual a {:.2f}'.format (va, seno))
cosseno= cos(radians(va))
print ('O cosseno de {:.2f} é igual a {:.2f}'.format(va, cosseno))
tangente= tan(radians(va))
print ('A tangente de {:.2f} é {:.2f}'.format(va, tangente))
