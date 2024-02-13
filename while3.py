v1 = int(input(" digite o valor inical "))
if v1 < 0 : print('Erro valor inicial deve ser natural')
else : 
    v2 = int(input(' digite o valor final '))
    if v2 < 0 : print('Erro valor final deve ser natural')
    else : 
        if v1 > v2 : 
            aux = v1
            v1 = v2
            v2 =aux
        if v1 % 2 == 0 : v1 = v1 +1
        soma =0
        print('V impar')
        while v1 <= v2:
            print(v1)
            soma = soma + v1
            v1 = v1 + 2
        print(f'S V Pares{soma}')