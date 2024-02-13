lista =[]
for cont in range(0,3):
    notas = float(input("Informe o valor da nota: "))
    lista.append(notas)

media = sum(lista)/len(lista)
maior = max(lista)
menor = min(lista)


print(lista)
print(" Média: ", media , "\n", "Maior: ", maior, "\n", "Menor: ", menor)