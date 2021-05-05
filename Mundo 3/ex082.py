# Exercício Python 082:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista_valores = list()
lista_par = list()
lista_impar = list()
continuar = 'S'

while continuar != 'N':

    valor_digitado = int(input("Digite um valor: "))
    lista_valores.append(valor_digitado)
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if continuar not in 'SN':
        continuar = str(input("Opção inválida,\nQuer continuar? [S/N] ")).strip().upper()[0]

print("Processando os dados...")
lista_valores.sort()

for valor in lista_valores:
    if valor % 2 == 0:
        lista_par.append(valor)
    if valor % 2 == 1:
        lista_impar.append(valor)
print(f"Então, a lista completa é {lista_valores}")
print(f"A Lista Par é {lista_par}")
print(f"A lista Impar é {lista_impar}")
