lista = []
cont = 0
while True:
    lista.append(int(input(f'Digite um valor: ')))
    opc = str(input('Quer Continuar ? S/N: ')).upper().split()
    if opc == 's':
        cont += cont
        if opc =='n':
           break
lista.sort()    
print(f'Foram digitados {cont} n na lista')  
print(f'Os valores digitados em ordem foram {lista}')  


