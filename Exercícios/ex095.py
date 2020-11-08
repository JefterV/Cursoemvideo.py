from time import sleep
jogadores = {}
todos = []
gols = []
while True:
    jogadores['nome'] = str(input('Nome: ')).capitalize()
    jogos = int(input('Quantos jogos?'))
    for j in range(0 , jogos):
        gols.append(int(input(f'{"": <5}Quantos gols no {j+1}º jogo? ')))
    jogadores['gols'] = gols[:]
    jogadores['total'] = sum(gols)
    todos.append(jogadores.copy())
    gols.clear()
    jogadores.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'S' or continuar == 'N':
            break
        print('Erro, Tente Novamente.',end=' ')
    if continuar == 'N':
        break

print('-'*40)
print(f'  {"Nome": <15} {"Gols": <13} {"Total"}')
print('=-'*20)
for k in range(0, len(todos)):
    print(f'{k+1} {todos[k]["nome"]: <15} {todos[k]["gols"]}{todos[k]["total"]}')
print('=-'*20)
while True:
    jogador = int(input('Mostrar dado de qual jogador? (999) interrompe '))
    if jogador == 999:
        break
    if jogador not in todos:
        print('Esse jogador não existe, tente novamente.')
        continue
    print('-'*40)
    print(f'  --  Levantamento do jogador {todos[jogador-1]["nome"]}')
    print('-'*40)
    for k in range(0, len(todos[jogador-1]['gols'])):
        print(f'{"": <10}No jogo {k+1} fez {todos[jogador-1]["gols"][k]} gols')
        sleep(1)
