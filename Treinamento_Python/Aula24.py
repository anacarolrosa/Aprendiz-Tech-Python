# Faça um programa que pergunte o valor de uma carro, 
# o valor do salario dele e em quantos anos ele vai querer pagar.
#  Calcule o valor da prestação mensal, sabendo  que ele nao pode exceder 30% do salario, se exceder,
#   retorne uma mensagem dizendo que foi negado

valor = float(input('Digite o valor do carro: '))
salario = float(input('Digite o valor do seu salario: '))
pagar_anos = int(input('Digite em quantos anos vai querer pagar: '))
meses = valor/(pagar_anos * 12)
if meses > (salario * 0.3):
    print('Negado, o valor excedeu seu salario!!')
else:
    print(f'O valor da prestacao eh: {meses:.2f}')
