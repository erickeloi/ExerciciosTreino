# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = list()
contador_soma_pares = contador_soma_coluna3 = maior_valor_linha2 = int()
for contador in range(0, 10):

    if 1 <= contador <= 3:
        valor = int(input(f"Digite o valor da elemento [1, {contador}]: "))
        matriz.append(valor)

        if valor % 2 == 0:
            contador_soma_pares += valor

        if contador == 3:
            contador_soma_coluna3 += valor

    elif 4 <= contador <= 6:
        valor = int(input(f"Digite o valor da elemento [2, {contador-3}]: "))
        matriz.append(valor)

        if valor % 2 == 0:
            contador_soma_pares += valor

        if contador == 6:
            contador_soma_coluna3 += valor

        if valor > maior_valor_linha2:
            maior_valor_linha2 = valor

    elif 7 <= contador <= 9:
        valor = int(input(f"Digite o valor da elemento [3, {contador-6}]: "))
        matriz.append(valor)

        if valor % 2 == 0:
            contador_soma_pares += valor

        if contador == 9:
            contador_soma_coluna3 += valor

print()
print("Gerando Matriz..")
print()

print(f'''[{matriz[0]}] [{matriz[1]}] [{matriz[2]}]\n[{matriz[3]}] [{matriz[4]}] [{matriz[5]}]\n[{matriz[6]}] [{matriz[7]}] [{matriz[8]}]''')
print()
print(f"A soma dos valores Pares é: {contador_soma_pares}")
print(f"A soma dos A soma dos valores da terceira coluna é: {contador_soma_coluna3}")
print(f"O maior valor da segunda linha é: {maior_valor_linha2}")

