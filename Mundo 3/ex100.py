# Exercício Python 100: Funções para sortear e somar
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia():
    numeros = list()
    print("Sortando 5 Números: ", end="")

    for c in range(0, 5):
        numero = randint(0, 10)
        print(f"{numero} ", end="")
        numeros.append(numero)
        sleep(0.3)

    print()

    return numeros


def somaPar(numeros):
    soma_par = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma_par += numero
    print(f"Os valores informados são: {numeros} e a soma dos valores pares é: {soma_par} ")


numeros = sorteia()
somaPar(numeros)
