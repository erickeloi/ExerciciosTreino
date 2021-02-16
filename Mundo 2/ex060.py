# Exercício 60
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
fatorial = 1
num = int(input("Digite um número: "))
contador = num
print(f"{num}! = ", end="")
while contador != 0:
    print(f"{contador} x " if contador !=1 else f"{contador} = ", end = "")
    fatorial = contador * fatorial
    contador -= 1
print(f'{fatorial}')
