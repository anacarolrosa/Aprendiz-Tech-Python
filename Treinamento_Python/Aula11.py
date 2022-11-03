# nome = input('Digite seu nome completo: ')
# print(nome.upper())
# print(nome.lower())
# #.upper() deixa todas as letras maisculas#
# #.lower() deixa todas as letras minusculas#

# print(nome.title())
# #Deixa as letras do começo do nome maiusculas#

# lista = nome.split()
# #Quando vc cria uma variavel que recebe outra variavle .split() a variavel que recebeu as informaçoes criam uma lista#
# print(nome.split())
# #.split() verifica a informaçao que esta dentro dela#

# print(len("".join(lista)))
# #.join() junta as informaçoes#
# print(len(lista))
# # len() conta a quantidade de elementos dentro da sua lista#

#entendendo na pratica como funciona#
info = 'Eu gosto; de python'
print(info.split(";"))
#split() separa/quebra em lista# 

info2 = '*'
print(info2.join(info))
#join() adiciona as informaçoes#
info3 = info2.join(info)
print(len(info3))