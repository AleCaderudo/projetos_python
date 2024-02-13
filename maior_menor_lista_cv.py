lista = []
for c in range(0,4):
    lista.append(int(input(f'Digite um valor para posição {c+1}: ')))
print(lista)
mai = max(lista)
maior = lista.index(mai)
menor = lista.index(min(lista))
print(f'O maior numero: {mai} na posição {maior+1}')
print(f'O menor numero: {min(lista)} na posição {menor+1}')