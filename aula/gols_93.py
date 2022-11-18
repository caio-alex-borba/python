jogo = {}
gols = []
jogo['nome'] = str(input('Nome do jogador: '))
jogo['jogos'] = int(input('Numero de jogos: '))
for i in range(jogo['jogos']):
    gols.append(int(input(f'Gols na {i+1} partida: ')))
jogo['gol'] = gols[:]
saldo = sum(jogo['gol'])
print('#'*43)
print(f'# O jogador {jogo["nome"]} teve um saldo de {saldo} gols. #')
print('#'*43)