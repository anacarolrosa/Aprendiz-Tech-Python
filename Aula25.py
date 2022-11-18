# Crie um progrma que leia o ano de 5 pessoas.
#  No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja são de maiores
from datetime import date
counter_maior = counter_menor = 0


for c in range (5):
    ano = int(input('informe o seu ano de nascimento: '))
    data = date.today().year - ano
    if data >= 18:
        counter_maior +=1
    else:
        counter_menor +=1
print(f'Ao todo tem {counter_maior} de maior e {counter_menor} de menor. ')