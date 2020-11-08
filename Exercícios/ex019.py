import random
a1= input('Primeiro aluno')
a2= input('Segundo aluno')
a3= input('Terceiro aluno')
a4= input('Quarto aluno')
lista= [a1, a2, a3,a4]
escolhido= random.choice (lista)
print ('O aluno escolhido foi {}'.format(escolhido))
print ('Agora vamos ver quem vai limpar as carteiras')
print ('')
print ('Sera o {}'.format(escolhido))