valor = float(input('Qual o valor da compra? R$'))
print('''Escolha uma das opções
[ 1 ] Pagamento a vísta dinheiro/cheque
[ 2 ] A vísta no cartão 
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Qual sua opção: '))
if forma == 1:
    desconto = valor - (valor * 10 / 100)
    print('Você ganhou um desconto de 10% e irá pagar R${:.2f}'.format(desconto))
elif forma == 2:
    desconto = valor - (valor * 5 / 100)
    print('Você ganhou um desconto de 5% e irá pagar  R${:.2f}'.format(desconto))
elif forma == 3:
    conta = valor / 2
    print('Você irá pagar em 2x no cartão. Por mês R${:.2f} no total R${:.2f}.'.format(conta, valor))
elif forma == 4:
    fm = int(input('Quantas parcelas: '))
    juros = valor + (valor * 20 / 100)
    fm1 = juros / fm
    print('Parcelando em {}x, você irá pagar por mês R${:.2f}. O valor total é R${:.2f}'.format(fm, fm1, juros))
else:
    print('Essa opção é invalida, tente novamente.')