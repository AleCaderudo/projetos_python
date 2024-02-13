import cv_modulo_sec

num = int(input('Digite um valor: '))
fat = cv_modulo_sec.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {cv_modulo_sec.dobro(num)}')
print(f'O triplo de {num} é {cv_modulo_sec.triplo(num)}')
