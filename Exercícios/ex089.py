Nome = []
Nota = []
s = []
while True:
    Nome.append(str(input('Nome: ')))
    s.append(float(input('Nota 1: ')))
    s.append(float(input('Nota 2:')))
    Nota.append(s[:])
    s.clear()
    continuar = str(input('Deseja continuar [S/N]: '))[0]
    if continuar == 'n':
        break
print('='*30)
print(f'{"Nome": ^15} {"Media": ^15}')
print('-'*30)
for p, c in enumerate(Nota):
    print(f'{p+1: <5}{Nome[p]:<15} {(Nota[p][0] + Nota[p][1]) / 2}')
while True:
    pe = int(input('Qual aluno você deseja saber a nota (999) interrompe:'))
    if pe == 999:
        break
    else:
        print(f'As notas de {Nome[pe+1]} foram {Nota[pe+1]}')