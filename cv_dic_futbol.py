dados = {}
time = []
partidas = []

while True:
    dados.clear()
    dados['nome'] = str(input('Digite o nome: '))
    qp = int(input(f'Digite a quantidade de jogos de {dados["nome"]}: '))
    partidas.clear()
    for c in range(0, qp):
        partidas.append(int(input(f'Digite a quantidade de gols na {c+1} partida: ')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opc in 'SN':
            break
            print('ERRO! digite apenas S ou N')
    if opc == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k+1:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<12} ', end='')
    print()
print('-' * 40)


