import BBC
n1 = float(input('Qual o seu salario? R$: '))
if n1 <= 1250:
    calculo = n1 + (n1 * 15 / 100)
else:
    calculo = n1 + (n1 * 10 / 100)
print(BBC.azuL,'O seu salario antes erá R${:.2F}, agora é R${:.2F}.'.format(n1, calculo))