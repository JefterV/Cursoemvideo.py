from datetime import datetime
atual = datetime.today().year
ano1 = int(input("Você nasceu em queal ano? "))
idade = atual - ano1
print ('Quem nasceu em {}, tem {} anos'.format(ano1, idade))
if idade <= 9:
    print ('A sua categoria é \033[30mMirim\033[m !!')
elif idade <= 14:
    print ('A sua categoria é \033[33mINFANTIL\033[m !!')
elif idade <= 19:
    print ('A sua categoria é \033[34mJUNIOR\033[m !!')
elif idade <= 25:
    print ('A sua categoria é \033[36mSÊNIOR\033[m !!')
else:
    print('A sua categoria é \033[37mMATER\033[m !!')