name0= str (input ('Qual o seu nome completo?')).strip()
print ('Analisando o seu nome...')
print ('Seu nome em letras maiúsculas {}'.format(name0.upper()))
print ('Seu nome em letras minúsculas {}'.format(name0.lower()))
n1= name0.replace(' ','')
print ('Seu nome contem {} letras e seu primeiro nome {} letras'.format(len(name0) - name0.count(' '), name0.find(' ')))




