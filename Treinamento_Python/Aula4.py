from curses.ascii import isalpha


algo = input('Digite algo: ')
print('O tipo primitivo desse valor eh: ',type(algo))
print('Tem espaço? ',algo.isspace())
print('Eh algo numerico? ', algo.isnumeric())
print('Tem alguma letra do alfabeto?',algo.isalpha())
print('Eh um alfa numerico?',algo.isalnum())
print('Eh uma letra maiuscula? ',algo.isupper())
print('Eh uma letra minuscula? ',algo.islower())