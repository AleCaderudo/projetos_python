temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    lista.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(lista)
print(f' {len(lista)} pessoas cadastradas')
for p in lista:
    if p[1] == maior:
        print(f'O maior peso {p[0]} com {p[1]} kg')
print()        
for p in lista:
    if p[1] == menor:
        print(f'O menor peso {p[0]} com {p[1]} kg')

        
