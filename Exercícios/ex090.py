


boletim = {}
boletim['nome']= str(input('Nome: '))
boletim['media']= float(input('Media: '))

print(f'O nome é {boletim["nome"]}')
print(f'Sua media é {boletim["media"]}')
if boletim['media'] < 5:
    print('A situação dele é reprovado')
else:
    if boletim['media'] <= 7:
        print('Você foi aprovado mais tome cuidado')
    if boletim['media'] >= 7:
        print('Você foi aprovado. PARABENS!')
