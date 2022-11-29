# Faça um programa que tenha uma função chamada fichajogador(), que receba dois parâmetros:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.


def fichajogador(nome, gols):
    return f"O jogador(a) {nome} fez {gols} gols."
    
nome = input('Digite seu nome: ')
gols = input('Digite a quantidade de gols: ')
if nome == '':
    nome = 'Desconhecido'
# else:
#     print(nome)
if gols.isnumeric() == 0:
   gols = 0
# else:
#     print(gols)
print(fichajogador(nome, gols))