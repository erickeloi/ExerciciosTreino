# Exercício 74
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randrange
Numeros = (randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10))
print(f"Os números sorteados são: {Numeros}")
print(f"Os números em ordem crescente são: {sorted(Numeros)[::-1]}")
print(f"Os números em ordem decrescente são {sorted(Numeros)}")
print(f"O Menor número é: {sorted(Numeros)[0]}\nE o Maior Número é: {sorted(Numeros)[-1]}")
