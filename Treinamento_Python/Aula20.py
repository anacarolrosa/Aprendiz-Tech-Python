preco = float(input("Digite o preço do produto: "))
opcao = input("Digite a opcao de pagamento: ")
dinheiro = preco - (preco * 10/100)
cartao = preco + (preco *15/100)
if opcao == 'dinheiro':
    print(f'voce tem 10% de desconto, o valor a pagar eh:  {dinheiro}')
elif opcao == 'cartao':
    print(f'voce tem 15% de juros, o valor a pagar eh: {cartao}')
else:
    print('Erro opcao invalida')