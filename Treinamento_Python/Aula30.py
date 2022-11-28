# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.media 
# No final, mostre o conteúdo da estrutura na tela.
# usando dicionario

aluno = dict()
aluno['nome'] = input('nome:')
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
if aluno['media'] >= 6:
    aluno['Situaçao'] = 'Aprovado'
elif aluno['media'] >= 4 and 5.9:
    aluno['Situaçao'] = 'Recuperaçao' 
else:
    aluno['Situaçao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')