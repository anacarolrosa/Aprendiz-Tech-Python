from random import choice

lista = []
lista.append(input('Informe o presente numero 1: '))
lista.append(input('Informe o presente numera 2: '))
lista.append(input('Informe o presente numera 3: '))
sorteado = choice(lista)
print(f'O presente sorteado p minha mãe foi: {sorteado}')

#Para próxima aula fazer usando o while