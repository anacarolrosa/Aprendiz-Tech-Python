def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)
    print(f"  {texto}")
    print("~" * tamanho)

def sla(txt):
    tamanho = len(txt) + 5
    print("=" * tamanho)
    print(f" {txt}")

escreva("Ana é programadora")
escreva("Curso de Python ")
escreva("Aprendiz Tech")

sla('sla12345')
sla('sla5678')
