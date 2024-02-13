#tabuada com for dentro de for
for numero in range(1,11): 
    for valor in range(1,11):
        print(numero , 'x' , valor , '=' , numero * valor)
    print()  
print('='*30)

# tabuada com while dentro de while
numero2 = 1
while numero2 <= 10:
    valor2 = 1
    while valor2 <= 10:
        print(numero2 , 'x' , valor2 , '=' , numero2 * valor2)
        valor2 = valor2 + 1
    print()
    numero2 = numero2 + 1
    print('-'*40)