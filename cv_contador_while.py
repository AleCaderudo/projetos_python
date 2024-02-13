def contador(i, f, p):
    """
    faz contagem e mostra na tela
    i é o inicio da contagem
    f é o fim da contagem
    p é o passo da contagem
    """
    cont = i
    while cont <= f:
        print(f' - {cont}', end='')
        cont = cont + p
    print(f'\n Fim')


i = int(input('Informe o n inicial: '))
f = int(input('Informe o n final: '))
p = int(input('Informe o passo'))
contador(i, f, p)

help(contador)