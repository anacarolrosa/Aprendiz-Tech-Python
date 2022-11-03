num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite o terceiro numero: '))
raiz = num1 ** (1/2)
print(f'A raiz quadrada num1 eh: {raiz}')

multiplicacao = num1 * num2
print(f'Multiplicando os valores num1 e num2 eh: {multiplicacao}')

soma = num1 + num2 
print(f'O resultado da soma eh: {soma} ')

subtracao = num1 - num2 
print(f'O resultado da subtração eh: {subtracao}')

divisao = num1 / num2
print(f'O resultado da divisão eh: {divisao}')



delta = (num2 ** 2) - 4 * num1 * num3

if num1 == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-num2 + delta ** (1 / 2)) / (2 * num1)
    x2 = (-num2 - delta ** (1 / 2)) / (2 * num1)

    print("x1: {}, x2: {}".format(x1, x2))
