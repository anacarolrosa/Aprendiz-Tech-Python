# Escreva um programa que pergunte o salario de um funcionario,
#  se o salario for igual ou superior a 1,250 reais,
#  calcule o aumento com 10%, para inferiores o aumento é de 15%,
#  e retorne o salario atualizado que ele terá com este aumento 

salario = float(input('Informe seu salario: '))
if salario >= 1.250:
    aumento = salario * 1.10
    print(f'Seu salario com aumento eh: {aumento}')
elif salario < 1.250:
    inferior = salario  * 1.15
    print(f'Seu salario com aumento eh: {inferior}')