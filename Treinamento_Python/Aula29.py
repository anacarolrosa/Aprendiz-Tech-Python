aluno = dict()
aluno['nome'] = str(input('nome:'))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5  <= aluno['media'] < 7:
     aluno['situaçao'] = 'Recuperaçao'
else:
    aluno['situaçao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')



# aluno = dict()
# nome = input('Digite seu nome:')
# media = float(input(f'Digite sua media {nome}: '))
# if media >= 7:
#     aluno['situação'] = 'Aprovado'
# elif 5 <= media < 7 :
#     aluno['situaçao'] = 'Recuperaçao'
# else:
#     aluno['Situaçao'] = 'Reprovado'
