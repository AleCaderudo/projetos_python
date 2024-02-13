#criar e gravar
arq = open("alturas.txt", "w")

cont = 1
while cont<=2:
    nome = input("Informe o nome: ")
    altura = input("Informe a altura: ")
    arq.write(nome + " - " + altura + "\n")
    cont =cont+1
arq.close()

#ler e calcula
lista = []
soma = 0
nomeM = ""
alturaM = 0
arq = open("alturas.txt", "r")
for linha in arq :
    saida = linha[:-1].split("-")
    altura = float(saida[1])
    nome = saida[0]
    dados= (nome,altura)
    soma = soma + altura

    if altura > alturaM :
        alturaM = altura
        nomeM = nome
    lista.append(dados)
arq.close()
print(lista)
print("Média: ", soma/len(lista))
print("Nome do mais alto: ", nomeM)
