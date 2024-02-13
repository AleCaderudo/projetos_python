arq = open('test.txt', 'r')
dados = []
for linha in arq:
    valores = linha.split(",")
    #print(valores)
    ultima = valores[4][:-1]
    tupla = (float(valores[0]) , float(valores[1]), float(valores[2]), float(valores[2]), ultima)
    dados.append(tupla)
    
arq.close()
print(dados)