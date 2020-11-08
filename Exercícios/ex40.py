m1 = float(input('Primeira nota: '))
m2 = float(input('Segunda nota: '))
media = (m1 + m2) / 2
if media < 5:
    print ("Você tem a media abaixo de 5.0, por esse motivo você está \033[31mRETIDO\033[m.")
elif 7 > media >= 5:
    print('Você está de recuperação a sua media é {}'.format(media))
elif media > 6.9:
    print('Você está \033[44maprovado')