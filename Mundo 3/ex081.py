# Exercício Python 081:
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_valores = list()
continuar = 'S'

while continuar != 'N':
    
    valor_digitado = int(input("Digite um valor: "))
    lista_valores.append(valor_digitado)
    continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    
    if continuar not in 'SN':
        continuar = str(input("Opção inválida,\nQuer continuar? [S/N]")).strip().upper()[0]
        
lista_organizada = lista_valores[:]
lista_organizada.sort(reverse=True)

print(f"Foram digitados {len(lista_valores)} números na lista")

print(f"A lista ordenada de forma decrescente é {lista_organizada}")

if 5 in lista_valores:
    print(f"O número 5 está na lista")
else:
    print(f"O número 5 não está na lista")
