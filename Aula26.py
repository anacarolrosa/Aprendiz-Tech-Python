#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No fim do progrma mostre:
# a media de idade dos grupos
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
soma = count_mulheres = maior = 0
for c in range(4):
    nome = input('Digite seu nome: ')
    idade= int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: ')
    soma = soma + idade
    media = soma/4
    if sexo == 'masculino'and idade > maior:
        maior = idade
        velho = nome
    if sexo == 'feminino' and idade <20:
        count_mulheres +=1
print(f'A media de idade dos grupos eh: {media}\n O nome do homem mais velho eh: {velho}\n Sao {count_mulheres} mulheres com menos de 20')
        
    
