import BBC
def cabeçalho():
    print(BBC.fazul,'-'*40)
    print(f'{"SISTEMA DE AJUDA": ^40}')
    print('-'*40)
    print(BBC.limpa, end='')

def acesso(msg):
    print(BBC.fmagenta,'#' * 40)
    print(f'      ACESSANDO O MANUAL DE {msg}')
    print('#'*40)
    print(BBC.limpa, end='')
def ajuda(msg):
    print(BBC.fazulc)
    help(msg)
    print(BBC.limpa, end='')
while True:
    cabeçalho()
    sobre = str(input('Digite a biblioteca que deseja conhecer: '))
    acesso(sobre)
    ajuda(sobre)