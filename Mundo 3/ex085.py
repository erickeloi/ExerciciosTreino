# Exercício Python 085:
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista_valores = list()
contador_par = contador_impar = 0
for contador in range(0, 7):
    valor = int(input(f"Digite o {contador+1}° valor: "))
    lista_valores.append(valor)

print("Processando...")
lista_valores.sort()

print(f"A lista de números pares é: ", end="")

for numero in lista_valores:
    if numero % 2 == 0:
        print(f"[{numero}]", end="")
print()

print(f"A lista de números impares é: ", end="")

for numero in lista_valores:
    if numero % 2 == 1:
        print(f"[{numero}]", end="")

print()

