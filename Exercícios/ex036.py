casa = float(input('Qual o valor da casa? R$:'))
salario = float(input('Nós informe o seu salario mensal? R$:'))
pagamento = float(input('Você pretende pagar em quantos anos? '))
# CALCULOS
c1 = salario * 30 / 100
c2 = pagamento * 12
c3 = casa / c2
# RESPOSTAS
print('Para você pagar uma casa de \033[31mR${:.2f}.\033[m As parcelas são de \033[31mR${:.2f}\033[m'.format(casa, c3 ))
if c3 > c1:
    print('Pedido \033[31mNEGADO\033[m')
else:
    print('Pedido \033[34mACEITO\033[m')