v1 = int(input("Digite o valor 1 "))
v2 = int(input("Digite o valor 2 "))
v3 = int(input("Digite o valor 3 "))

lista = v1, v2, v3
ordenada = sorted(lista)
print("Em ordem crescente " , ordenada)

maior = v1
if v2>maior : maior =v2
if v3>maior : maior = v3
print("Maior numero" , maior)

menor = v1
if v2<menor : menor = v2
if v3<menor : menor = v3
print("Menor numero" , menor)

meio = v1+v2+v3 - maior - menor
print("Numero do meio" , meio)
