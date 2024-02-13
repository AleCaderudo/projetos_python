enq = int(input('Digite um n inteiro valido: '))
while enq<=0 : 
    print('Numero invalido')
    enq = int(input('Digite um n inteiro valido: '))

num =2
primos =1
while primos <= enq :
    divisor = 0
    d=1
    while d <= num :
        if num % d == 0 : divisor = divisor + 1
        d = d+1
    if divisor == 2 :
         print(num) 
         primos = primos + 1
    num = num +1