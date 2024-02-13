nt = int(input(" informe numeros naturais "))
if nt <=0 : print(" N invalido")
else:
    soma = 0
    cont =1
    while cont<= nt :
        soma = soma + 1/cont
        cont = cont +1
    print(f' Soma {soma:.3f}')