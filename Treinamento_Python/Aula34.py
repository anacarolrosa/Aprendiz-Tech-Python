#Faça um programa que tenha uma função chamada calcular()

def calcule(x, y):
    resultado = x + y
    return resultado

def pergunta():
    x = int(input('Digite seu primeiro num: '))
    y = int(input('Digite seu segundo num: '))
    print(calcule(x, y))

while True:
    pergunta()
    break
