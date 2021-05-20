# Exercício Python 108: Formatando Moedas em Python
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from ex108 import moeda
from time import sleep

while True:
    print("""
    [ 1 ] - Dobrar
    [ 2 ] - Metade
    [ 3 ] - Aumentar
    [ 4 ] - Diminuir
    [ 0 ] - Finalizar programa""")
    operacao = int(input("\nQual operação você deseja realizar? "))
    if operacao == 0:
        break
    elif operacao == 1:
        valor = float(input("Digite um valor para ser dobrado: R$"))
        print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}")
    elif operacao == 2:
        valor = float(input("Digite um valor para ser reduzido a metade: R$"))
        print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
    elif operacao == 3:
        valor = float(input("Digite o valor base: R$"))
        porcentagem = float(input("Digite a porcentagem de acrescimo: "))
        print(f"O valor {moeda.moeda(valor)} tendo um acrescimento de {porcentagem}% é: {moeda.moeda(moeda.aumentar(valor, porcentagem))}")
    elif operacao == 4:
        valor = float(input("Digite o valor base: R$"))
        porcentagem = float(input("Digite a porcentagem de decrescimo: "))
        print(f"O valor {moeda.moeda(valor)} tendo um decrescimo de {porcentagem}% é: {moeda.moeda(moeda.aumentar(valor, porcentagem))}")

    else:
        print("Opção inválida!")
    sleep(4)
