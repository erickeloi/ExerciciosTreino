# Exercício 75
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os Números Pares.
NumPar = 0
num1 = int(input("Digite um número: "))
num2 = int(input(("Digite outro número: ")))
num3 = int(input(("Digite outro número: ")))
num4 = int(input(("Digite outro número: ")))
Numeros = (num1, num2, num3, num4)
print(f"Os números digitados foram: {Numeros}")
print(f"O número '9' apareceu {Numeros.count(9)} Vezes")
if 3 in Numeros:
    print(f"O número '3' foi digitado pela primeira vez no {Numeros.index(3)+1}º Número")
else:
    print("O número '3' não foi digitado")
print("Os números pares digitados foram: ", end='')
for numero in Numeros:
    if numero % 2 == 0:
        print(f"{numero} ", end='')

