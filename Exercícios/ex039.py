from datetime import datetime
ano1 =  int(input('Ano de nascimento: '))
ano2 = datetime.today().year
ano3 = ano2 - ano1
ano4 = ano3 - 18
ano5 = (18 - ano3) + ano2
ano6 = ano1 + 18
print(('Quem nasceu em {}, tem {} anos em {}').format(ano1, ano3, ano2))
if ano3 == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
elif ano3 <=17:
    print ('Seu alistamento será em {}.'.format(ano5))
elif ano3 >= 19:
    print('Seu alistamento já passou á {} anos. \nvocê deveria ter se alistado em {}.'.format(ano4,ano6))

exit()