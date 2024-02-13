def num(*n):
    d = {}
    # conta e inclui no dicionaruo quantos itens foram digitados
    d['total'] = len(n)
    # maior numero digitado
    d['maior'] = max(n)
    # menor numero digitado
    d['menor'] = min(n)
    # media
    d['media'] = (sum(n) / len(n))

    return d


resp = num(1, 6, 32, 78, 7)
print(resp)