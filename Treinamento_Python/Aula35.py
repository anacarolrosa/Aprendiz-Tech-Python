# Faça um programa que tenha uma função chamada area(),
#  que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento):
    area_terreno = largura * comprimento
    return area_terreno
    
def informe():
    largura = float(input('Informe a largura do terreno: '))
    comprimento = float(input('Informe o comprimento do terreno: '))
    print(area(largura, comprimento))

while True:
    informe()
    break
  
    
