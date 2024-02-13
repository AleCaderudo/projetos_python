def conta(m1, m2):
    tam = m1 * m2
    print(f'A soma de {m1} m e {m2} m é igual a {tam:3} m²')


print('-'*30,  '\n     Controle de terrenos\n',  '-'*30)
m1 = float(input('Digite a largura do terreno: '))
m2 = float(input('Digite o comprimento do terreno: '))
conta(m1, m2)