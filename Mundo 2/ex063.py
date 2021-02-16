# Exercício 63
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print("-"*30)
print("Programa Sequência de Fibonacci")
print("-"*30)
termos = int(input("Quantos termos você deseja mostrar? "))
termo1 = 0
termo2 = 1
contador = 3
if termos == 1:
    print(" 0 ")
elif termos == 2:
    print(" 0 -> 1")
else:
    print(" 0 -> 1 ->", end='')
    while contador <= termos:
        termo3 = termo1 + termo2
        print(f" {termo3} ->", end="")
        termo1 = termo2
        termo2 = termo3
        contador += 1
print("FIM")
