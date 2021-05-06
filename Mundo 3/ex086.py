# Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = list()
for contador in range(0, 10):

    if 1 <= contador <= 3:
        valor = int(input(f"Digite o valor da elemento [1, {contador}]: "))
        matriz.append(valor)

    elif 4 <= contador <= 6:
        valor = int(input(f"Digite o valor da elemento [2, {contador-3}]: "))
        matriz.append(valor)

    elif 7 <= contador <= 9:
        valor = int(input(f"Digite o valor da elemento [3, {contador-6}]: "))
        matriz.append(valor)

print()
print("Gerando Matriz..")
print()

print(f'''[{matriz[0]}] [{matriz[1]}] [{matriz[2]}]\n[{matriz[3]}] [{matriz[4]}] [{matriz[5]}]\n[{matriz[6]}] [{matriz[7]}] [{matriz[8]}]''')

