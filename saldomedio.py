saldo = float(input("Digite o saldo "))
if saldo < 500 : print("Sem Limite")
if saldo >= 500 and saldo < 1000 : print("Saldo medio" , saldo *8 / 100)
if saldo >1000 : print("Saldo medio" , saldo * 0.15)
