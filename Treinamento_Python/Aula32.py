# Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no da
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'jogador1':randint(1,6), 
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)
}
resultado = list()
for k, v in jogadores.items():
    print(f'O {k} recebeu o valor de {v}')
    sleep(2)

resultado = sorted(jogadores.items(),key = itemgetter(1),reverse = True)
print("O resultado dos jogadores")

for i , u in enumerate(resultado):
    print(f'Em {i+1} lugar: {u[0]} com {u[1]} ')