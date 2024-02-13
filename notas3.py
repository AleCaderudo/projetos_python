print("Digite notas  1 a 10")
n1 = float (input(" digite nota 1 "))
n2 = float (input(" digite nota 2 "))
n3 = float (input(" digite nota 3 "))

if n1<0 or n1>10 or n2<0 or n2>10 or n3<0 or n3>10 : print("Errrrro")
else :
    maior = n1
    if n2>maior : maior = n2
    if n3>maior : maior = n3
    media = 0.5 * maior + 0.25 * (n1+n2+n3-maior)
    print("Mdia ponderada : " , media)