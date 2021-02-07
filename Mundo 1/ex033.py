# Desafio 33
# lê três números e mostra qual o maior e qual o menor
num1 = float(input("Digite aqui o primeiro número: "))
num2 = float(input("Digite aqui o segundo número: "))
num3 = float(input("Digite aqui o terceiro número: "))
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f"Então, o menor número é o {menor},\nE o maior número é o {maior}")
