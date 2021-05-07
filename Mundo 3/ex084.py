# Exercício Python 084:
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_pessoas = list()
lista_complementar = list()
maior_peso = menor_peso = contador_pessoas = 0

while True:
    nome = str(input("Digite o nome da pessoa: "))
    peso = int(input("Digite o peso da pessoa: "))

    if len(lista_pessoas) == 0:
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

    lista_complementar.append(nome)
    lista_complementar.append(peso)

    lista_pessoas.append(lista_complementar[:])

    lista_complementar.clear()

    contador_pessoas += 1

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input("Opção inválida,\n Quer continuar? [S/N]: "))
    if continuar == 'N':
        break
print("Processando...\n")
print(f"Foram cadastradas {contador_pessoas} Pessoas")
print(f"Essas pessoas, com seus pesos foram: {lista_pessoas}")

print(f"As pessoas mais pesadas são: ", end="")
for pessoa in lista_pessoas:
    if pessoa[1] == maior_peso:
        print(f"{pessoa[0]} com {pessoa[1]} KG...", end="")
print("")

print(f"As pessoas mais leves são: ", end="")
for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(f"{pessoa[0]} com {pessoa[1]} KG...", end="")
print("")

