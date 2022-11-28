# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário. 
# Se por acaso a carteira de trabalho for diferente de zero, o dicionário receberá também
# o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos
# a pessoa vai se aposentar.
# Obs.: aposentadoria em 35 anos de contribuição.
from datetime import datetime
pessoa = dict()

pessoa['nome'] = input('nome: ')
pessoa['ano'] = int(input(f'Digite seu ano de nascimento {pessoa["nome"]}: '))
pessoa['idade'] = datetime.now().year - pessoa["ano"]
pessoa['carteira'] = int(input('Digite o numero da sua carteira de trabalho, caso não tenha uma carteira digite 0: '))

if pessoa['carteira'] != 0:
   pessoa['contratada'] = int(input('digite o ano de sua contrataçao: '))
   pessoa['salario'] = float(input('digite o Salário: ')) 
   pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratada']+35)- datetime.now().year)
else:
    print('Para vc se aposentar vc precisa ser contratado(a)')

for k, v in pessoa.items():
    print(f'{k} O valor dessa variavel eh: {v}')











