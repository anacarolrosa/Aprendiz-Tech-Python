def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res

def diminuir(preco, taxa):
    res = preco - (preco*taxa/100)
    return res

def dobro(preco, taxa):
    res = preco * 2
    return res

def metade(preco, taxa):
    res = preco / 2 
    return res

def formata(preco, taxa, moeda = "$"):
    return f"{moeda} {preco:.2f} {taxa:.2f}".replace(".",",")
    