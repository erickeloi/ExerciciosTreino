#Desafio 10
#Programa comprador de dolares
#Lê certa quantia de dinheiro e mostra quantos dolares é possível comprar.
#Futuramente quero usar uma API para ver em tempo real quanto é a cotação do dolar e converter de forma "correta" com precisão
dinheiro = float(input("Digite aqui sua quantidade de dinheiro (em Reais / BRL ) que deseja comprar em dólar (USD): "))
dolar = dinheiro/3.27
print(f"Você possui {dinheiro} BRL e pode comprar {dolar:.2f} USD\n Cotação do dolar: 1USD = 3.27 BRL")
