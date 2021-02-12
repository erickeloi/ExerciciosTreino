# Desafio 55
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for contador in range(1, 6):
    peso = float(input(f"Digite aqui o peso da {contador}º pessoa"))
    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"Então, o maior peso é {maior}Kg/F e o menor peso é {menor}Kg/F")
