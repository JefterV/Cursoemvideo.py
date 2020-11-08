import random
a1= input('Primeiro nome: ')
a2= input('Segundo nome: ')
a3= input('Terceiro nome: ')
a4= input('Quarto nome: ')
lista= [a1, a2 , a3, a4]
random.shuffle (lista)
print ('A ordem será {}'.format (lista))