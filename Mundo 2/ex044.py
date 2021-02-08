# Desafio 44
# Lê um preço de um produto e sua condição de compra para fazer as devidas operações:
# Regras de negócio:
# A vista: Dinheiro/Cheque == 10% de desconto
# A vista: Cartão == 5% de desconto
# Em até 2x no cartão == Preço normal
# 3x ou mais no cartão == 20% de juros
valorproduto = float(input("Digite o valor do produto: "))
forma = int(input("Digite 1 para pagar a vista no Dinheiro/cheque (10% de desconto)\n"
                  "Digite 2 para pagar a vista no Cartão (5% de desconto)\n"
                  "Digite 3 para pagar em até 2x no cartão (Preço normal)\n"
                  "Digite 4 para pagar em 3x ou mais no cartão (20% de juros)\n"
                  "Opção: "))
if forma == 1:
    print(f"A vista no Dinheiro/cheque (10% de desconto),\n"
          f"O produto de {valorproduto}R$, com desconto de 10%, ficará por {valorproduto*0.9}R$\n"
          f"Ou seja, desconto de {valorproduto*0.1}R$ no preço do produto")
elif forma == 2:
    print(f"A vista no Cartão (5% de desconto)\n"
          f"O produto de {valorproduto}R$, com desconto de 10%, ficará por {valorproduto*0.95}R$\n"
          f"Ou seja, desconto de {valorproduto*0.05}R$ no preço do produto")
elif forma == 3:
    print(f"Até 2x no Cartão (Preço normal)\n"
          f"O produto ficará {valorproduto}R$ em até 2x no cartão")
elif forma == 4:
    print(f"Em 3x ou mais no Cartão (20% de juros)\n"
          f"O produto de {valorproduto}R$, com juros de 20%, ficará por {valorproduto*1.2}R$\n"
          f"Ou seja, aumento de {valorproduto*0.2}R$ no preço final do produto, parcelado em 3x ou mais.")
else:
    print("Digite uma opção válida")
