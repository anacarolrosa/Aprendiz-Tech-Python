#Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.
#Faça também um programa que importe esse módulo e use algumas dessas funções.
#Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.
# o 'diminuir()', mesma coisa.
import moeda

p = float(input('Digite:'))
m = float(input('Digite:'))
print(moeda.aumentar(p,m))
print(moeda.diminuir(p,m))
print(moeda.dobro(p,m))
print(moeda.metade(p,m))
