# faça um programa que verifique o sexo da pessoa se é M ou F e que se for diferente disso,
#  peça para que digite novamente ate obter o valor correto

digite = input('Digite seu sexo: ')
while digite not in 'FM':
    digite = input("Digite novamente: ")
print("fim")

# sexo = input("digite sexo da pessoa:")

# while sexo not in 'MF':
#     sexo = input("SEXO INVALIDO! DIGITE O SEXO NOVAMENTE")

# print(sexo)