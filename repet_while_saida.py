resp ="S"
media = soma = quant = 0
plural = ''
while resp in 'Ss':
    num = int(input(f'Digite um numero: '))
    soma += num
    quant += 1


    resp= str(input(f'Digite S para continuar ou N para parar : ')).upper().strip()[0]
media = soma / quant
if quant == 1: plural = ''
else: plural = 's'
print(f"Voce digitou {quant} numero{plural}, e a soma dele{plural} é {soma}")