
peso1 = int(input('Digite seu peso: '))
peso2 = int(input('Digite seu peso: '))
peso3 = int(input('Digite seu peso: '))
maior = peso1
if (peso2 > maior):
    maior = peso2
if (peso3 > maior):
    maior = peso3
print(f'O peso maior eh: {maior}')

menor = peso1
if (peso2 < menor):
     menor = peso2
if (peso3 < menor):
      menor = peso3
print(f'O peso menor eh: {menor}')
