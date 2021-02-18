# Exercício 70
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
contador_produto_maior1000 = total = contador = preco_mais_barato = 0
nome_produto_barato = ""
print("Sistema de Preços da Loja !")
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input(("Digite o preço do produto: ")))
    contador += 1
    if contador == 1:
        nome_produto_barato = nome
        preco_mais_barato = preco
    if preco < preco_mais_barato:
        nome_produto_barato = nome
        preco_mais_barato = preco
    if preco > 1000:
        contador_produto_maior1000 += 1
    total = preco + total
    continuar = str(input("Deseja Adicionar mais um produto? [S/N]")).strip().upper()[0]
    while continuar not in "SN":
        print("Digite uma opção válida!")
        continuar = str(input("Deseja Adicionar mais um produto? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
print("Fim do programa!")
print(f"O total gasto foi {total}\nNúmeros de produtos que custam mais de R$1000: {contador_produto_maior1000} produto(s)")
print(f"O nome do produto mais barato é '{nome_produto_barato}', custando: {preco_mais_barato}R$")
