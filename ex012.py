#Desafio 12
#Programa Calculador de desconto
#Lê um valor e um desconto e calcula o preço final com desconto
valor = float(input("Digite aqui o valor do produto: "))
desconto = float(input("Digite aqui o valor do desconto, em porcentagem: "))
preco = valor * (100 - desconto)/100
print(f"Então, o produto que custa {valor}, com o desconto de {desconto}, ficaria por {preco}")
