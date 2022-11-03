num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
if num1 > num2 > num3:
    print(f'O peimeiro numero eh o maior:  {num1}')
    if num2 > num1 > num3:
        print(f'O segundo numero eh o maior: {num2}')
else:
   print(f'O terceiro numero eh o maior: {num3}')
