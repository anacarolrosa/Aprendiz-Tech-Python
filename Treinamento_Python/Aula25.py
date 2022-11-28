# Crie um programa que leia o ano de 5 pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são de maiores
# a partir da  data de importação datetime  
contador_maior  =  contador_menor  =  0


for c in range (5):
    ano = int(input('informe o seu ano de nascimento: '))
    data = date.today().year - ano
    if data >= 18:
        contador_maior +=1
    else:
        contador_menor +=1
print(f'Ao todo tem {contador_maior} de maior e {contador_menor} de menor. ')


