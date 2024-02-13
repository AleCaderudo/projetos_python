aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Nota do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    print(f'O aluno {aluno["nome"]} com media {aluno['media']} foi aprovado')
elif 5 <= aluno ['media'] < 7:
    print(f'O aluno {aluno["nome"]} com media {aluno['media']} esta em recuperação')
else:
    print(f'O aluno {aluno["nome"]} com media {aluno['media']} foi reprovado')
print(aluno)
