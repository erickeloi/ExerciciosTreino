# Desafio 52
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
divisoes = 0
num = int(input("Digite um número inteiro para saber se ele é primo: "))
for contador in range(1, num+1):
    if num % contador == 0:
        print(f"\033[31m{contador}\033[m", end=" ")
        divisoes = divisoes + 1
    else:
        print(f"\033[37m{contador}\033[m", end=" ")
if divisoes == 2:
    print(f"\n Então, {num} é um número primo!!!")
    print(f"Pois, foi divisível duas vezes")
else:
    print(f"\nEntão, {num} não é um número primo!!!")
    print(f"Pois, foi divisível {divisoes} vezes")
    
