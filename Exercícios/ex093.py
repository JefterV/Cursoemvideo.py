jogador = {}
partidas = []
total = 0
jogador['nome'] = str(input('Nome: '))
tot_partidas = int(input('Total de partidas: '))
for p in range(0, tot_partidas):
    num = int(input(f'Quantos gols ele fez na {p}ª partida: '))
    partidas.append(num)
    total = num + total
    jogador['gols'] = partidas[:]

print('#=' * 25)
print(jogador, total)
print('#=' * 25)
