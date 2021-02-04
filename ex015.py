#Exercício Python 15:
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = 1
dia = int(input("Digite a quantidade de dias que o carro esteve alugado: "))
km = float(input("Digite a quantidade de Kilometros percorridos: "))
preco = (60*dia) + (0.15*km)
print(f"Então, você pagará {preco} Reais")
