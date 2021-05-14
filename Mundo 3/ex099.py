# Exercício Python 099: Função que descobre o maior
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint


def maior(* numeros: int):
    if len(numeros) == 0:

        print("-=" * 30)
        print("Não foram informados números")
        print("-=" * 30)

    if len(numeros) > 0:
        numeros = sorted(numeros)
        print("-=" * 30)

        print(f"Analisando os dados...\n"
              f"Nos número(s): {numeros}\n"
              f"Foram informado(s): {len(numeros)} ao todo\n"
              f"O maior número foi {numeros[-1]}")

        print("-=" * 30)

    print()


maior(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior(randint(0, 100), randint(0, 100))
maior(randint(0, 100))
maior()
