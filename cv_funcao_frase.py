def frase(fra):
    num = len(fra)+6
    print(f'-' * num)
    print(f'   {fra}')
    print(f'-' * num)


fra = input('Digite uma frase: ')
frase(fra)
