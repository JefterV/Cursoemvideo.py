from random import choice
import winsound
# VARIAVEIS
pd = str('Pedra')
pp = str('Papel')
ts = str('Tesoura')
lista = [pd, pp, ts]
escolha = choice(lista)
# INTERFACE
print ('''SUAS OPÇÕES
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
pergunta = int(input('Qual sua opção: '))
if pergunta == 1:
    m = str('Pedra')
elif pergunta == 2:
    m = str('Papel')
elif pergunta == 3:
    m = str('Tesoura')
from time import sleep
# INTERAÇÃO
winsound.PlaySound('coração1.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP | winsound.SND_NOSTOP)
print('JO')
sleep(1.5)
print('KEN')
sleep(1)
print('PO !!!')
sleep(0.5)
# RESULTADO
print('-='*13)
print('O JOGADOR JOGOU {} \nCOMPUTADOR JOGOU {}'.format(m,escolha))
print('-='*13)
# Estrutura do JOGO
import winsound
if pergunta == 3 and escolha == pd:
    print('EU GANHEI, valeu meu pato.')
    winsound.PlaySound('pulso1.wav',winsound.SND_FILENAME)
elif pergunta == 2 and escolha == ts:
    print('EU GANHEI, valeu meu pato.')
    winsound.PlaySound('pulso1.wav',winsound.SND_FILENAME)
elif pergunta == 1 and escolha == pp:
    print('EU ganhei, valeu meu pato.')
    winsound.PlaySound('pulso1.wav',winsound.SND_FILENAME)
elif pergunta == 1 and escolha == ts:
    print('Você ganhou. EU ASSUMO, SOU SEU PATO.')
elif pergunta == 3 and escolha == pd:
    print('Você ganhou. EU ASSUMO, SOU SEU PATO.')
elif pergunta == 2 and escolha == pd:
    print('Você ganhou. EU ASSUMO, SOU SEU PATO.')
elif pergunta == 3 and escolha == pp:
    print('Você ganhou. EU ASSUMO, SOU SEU PATO.')
elif m == escolha:
    print('Ora, Ora, temos um empate aqui, eu também coloquei {}'.format(escolha))

