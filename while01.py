# calculo numeros primos
val = int(input("Digite o valor "))
cont = 0
d = 1
while d <= val : 
    if val % d == 0 : cont = cont + 1
    d = d+1
if cont == 2 : print(f"{val}, é primo")
else : print(f"{val} não é primo")
