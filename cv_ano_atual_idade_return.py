def voto(ano):
    import datetime
    anoa = datetime.date.today().year
    print(f'Ano atual {anoa}')
    resultado = anoa - ano
    return resultado


ano = int(input('Digite o ano de nascimento: '))
res = voto(ano)
print(f'Sua idade {res}')