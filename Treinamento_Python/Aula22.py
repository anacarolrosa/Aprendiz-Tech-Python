# Faça um programa que pergunte a distancia em Km, se a distancia for menor que  200km,
# o preço da passagem é de 1.00 real se for maior, o valor da passagem é de 2.00 reais, 
# e retorne o valor que vou gastar em reais 


distancia = float(input('Digite a distancia em KM: '))
if distancia < 200:
   print(distancia * 1.00)
else:
    print(distancia * 2.00)