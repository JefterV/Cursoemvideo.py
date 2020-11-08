from datetime import datetime

def voto(ano):
    atual = datetime.now().year
    idade = atual - ano
    print(f'Com {idade} anos. ',end='')
    if idade <= 15:
        print('NÃO VOTA')
    elif 16 <= idade <= 17:
        print('VOTO OPCIONAL')
    elif idade >= 18 and idade <=64:
        print('VOTO OBRIGATORIO')
    elif idade >= 65:
        print('VOTO OPCIONAL')

voto(int(input('Você nasceu em que ano? ')))