# usando o mesmo desafio, crie uma função chamada formata() que formate os valores em reais
#       (se vc digitar 5, tem que retornar em formato de reais -> 5,0)

import moeda

p = float(input('Digite:'))
m = float(input('Digite:'))
print(moeda.formata(p,m))