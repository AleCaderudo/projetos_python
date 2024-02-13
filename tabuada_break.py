
while True:
    num = int(input('Digite um numero para mostrar a tabuada: '))
    print('-'*30)
    if num < 0 :
            break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
        #num =int(input(f'Para continua digite outro numero inteiro e para parar digite um numer negativo: '))
        

    print('-'*30)
print('Fim...')