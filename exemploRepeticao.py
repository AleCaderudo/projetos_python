# Media 10 alturas

soma = 0
maior = 0
repet = int(input('digite a quantidade de vezes que deseja repetir :'))
for cont in range(repet): 
    # codigo para random - import random - alt = random.uniform(1.3,1.9)
    alt = float(input("digite a altura "))
    soma = soma + alt
    if alt > maior : maior = alt

media = soma/repet
print(f"A media da altura é : {media:.3f}, e a maior altura é : {maior:.3f}")
