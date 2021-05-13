# Exercício Python 098: Função de Contador
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)

    print(f"Contando de {inicio} até {fim} indo de {passo} em {passo}")

    if fim < inicio:
        passo = -passo

        for numero in range(inicio, fim-1, passo):
            print(numero, end=" ")
            sleep(0.3)

    else:
        for numero in range(inicio, fim+1, passo):
            print(numero, end=" ")
            sleep(0.3)

    print("Fim!")
    print()


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez!")

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor de passo: "))

contador(inicio, fim, passo)
