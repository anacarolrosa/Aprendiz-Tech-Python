# Faça um programa que tenha uma função chamada maior(), que receba valores inteiros.
# Seu programa tem que analisar e dizer qual deles é o maior

# def maior(a, b):

#     if a > b:
#         print(a)
#     else:
#         print(b)

# a = int(input('Digite um valor: '))
# b = int(input('Digite outro valor: '))
# maior(a,b)

# def maior(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# def pergunta():
#     a = int(input('Digite um valor: '))
#     b = int(input('Digite outro valor: '))
#     maior(a,b)
# pergunta()

def maior(*argse):
    maior = 0
    print("Valores informados: ", end="")
    for i in argse:
        print(f"{i} ", end="")

    if len(argse) == 0:
      print(f"O maior valor informado foi {maior}")
    else:
      maior = max(argse)
      print(f"O maior valor informado foi {maior}")



maior(2, 9, 4, 5, 7, 1)
maior( 5, 7, 1)