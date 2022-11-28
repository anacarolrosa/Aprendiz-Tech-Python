# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

numeros = []

def sorteio():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    num3 = randint(1, 10)
    num4 = randint(1, 10)
    num5 = randint(1, 10)
    numeros.append(num1)
    numeros.append(num2)
    numeros.append(num3)
    numeros.append(num4)
    numeros.append(num5)
    print(f' O valor sorteado eh: {num1}  \n  O valor sorteado eh: {num2} \n  O valor soretado eh: {num3} \n  o valor soretado eh: {num4} \n O valor sorteado eh:  {num5} ')
sorteio()

def soma_par(lista):
    par = 0
    impar = 0
    for valor in lista:
        if valor % 2 == 0:
            par += valor
        else:
            impar += valor 
    print(f'A soma de todos os valores impares {lista} eh igual a: {impar}')
    print(f'A soma de todos os valores pares {lista} eh igual a: {par}')

soma_par(numeros)
