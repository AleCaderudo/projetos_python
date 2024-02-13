arq = open ("test.txt", "a")
cont = 1
while cont <= 3:
    nome = input("Informe um nome : ")
    arq.write(nome + "\n")
    cont = cont + 1
arq.close()