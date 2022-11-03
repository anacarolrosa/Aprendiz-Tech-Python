from datetime import date
data_atual = date.today().year

aluno = int(input("Informe o ano de seu nascimento: "))
data = data_atual - aluno
if data <= 11:
  categoria = 'mirim'
elif data <= 14:
  categoria = 'infantil'
elif data <= 18:
  categoria =  'adolescente'
elif data >=  19:
   categoria = 'adulto'
elif data <= 0:
   print("Ano invalido")
else: 
    print('Categoria error')
print(f'O aluno possui {data} e esta na categoria {categoria}')


