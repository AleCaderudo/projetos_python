try:
    n = int(input('Informe o numerador: '))
    d = int(input('Informe o denominador: '))
    r = n/d
except (ValueError, TypeError):
    print('Problema com o tipo de dados digitados')
except ZeroDivisionError:
    print('Não pode dividir por zero')
except KeyboardInterrupt:
    print('O usuario não digitou nada')
except Exception as erro:
    print(f'Erro de {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre')