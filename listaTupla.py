pecas = []
for i in range(0,3):
    print('Cont: ' , i)
    tamanho = input("Digite o tamanho, P,M,G :")
    while (tamanho!='p' and tamanho!='m' and tamanho!='g' ):
        tamanho = input("Digite o tamanho, P,M,G :")
    op = int(input("Digite a cor, 1-Preto, 2-Branco, 3-Azul: "))
    while(op<1 or op>3):
        op = int(input("Digite a cor, 2-Preto, 1-Branco, 3-Azul: "))
    if op==1 : tupla = (tamanho, "branco")
    else:
        if op==2 : tupla = (tamanho, "preto")
        else : tulpa = (tamanho, "azul")
    pecas.append(tupla)
    print(pecas)

