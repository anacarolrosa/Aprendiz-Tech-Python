ano = int(input('Digite o ano: '))
if (ano%4 == 0) and (ano%100 != 0) or (ano%400 == 0):
    print('Bissexto')
else:
    print('Não eh Bissexto')




# from calendar import isleap

# ano = int(input('Digite o ano: '))

# if isleap(ano):
#     print('É bissexto')
# else:
#     print('Não é bissexto')



# ano = int(input('Digite o ano: '))

# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano % 400 == 0:
#             print('Bissexto')
#         else:
#             print('Nao eh Bissexto')
#     else:
#         print('Bissexto')
# else:
#     print('Nao eh Bissexto')