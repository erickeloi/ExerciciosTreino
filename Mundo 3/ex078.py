# Exercício Python 78
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista_valores = list()
maior_valor = 0
menor_valor = 0
for c in range(0, 5):

    numero_digitado = (int(input(f"Digite o {c + 1}º valor: ")))
    lista_valores.append(numero_digitado)
    if c == 0:
        menor_valor = numero_digitado
    if numero_digitado > maior_valor:
        maior_valor = numero_digitado
    if numero_digitado < menor_valor:
        menor_valor = numero_digitado

lista_organizada = lista_valores[:]
lista_organizada.sort()

print(f"O maior valor digitado foi: {lista_organizada[4]}, e ele estava nas posições: ", end="")
for contador, valor in enumerate(lista_valores):
    if valor == maior_valor:
        print(f"{contador+1}...", end="")
print("")

print(f"O menor valor digitado foi: {lista_organizada[0]}, e ele estava nas posições: ", end="")
for contador, valor in enumerate(lista_valores):
    if valor == menor_valor:
        print(f"{contador+1}...", end="")
print("")

