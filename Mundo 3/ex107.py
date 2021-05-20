from ex107 import moeda
from time import sleep

while True:
    print("""
    [ 1 ] - Dobrar
    [ 2 ] - Metade
    [ 3 ] - Aumentar
    [ 4 ] - Diminuir
    [ 0 ] - Finalizar programa""")
    operacao = int(input("\nQual operação você deseja realizar?"))
    if operacao == 0:
        break
    elif operacao == 1:
        valor = float(input("Digite um valor para ser dobrado: "))
        print(moeda.dobro(valor))
    elif operacao == 2:
        valor = float(input("Digite um valor para ser reduzido a metade: "))
        print(moeda.metade(valor))
    elif operacao == 3:
        valor = float(input("Digite o valor base: "))
        porcentagem = float(input("Digite a porcentagem de acrescimo: "))
        print(moeda.aumentar(valor, porcentagem))
    elif operacao == 4:
        valor = float(input("Digite o valor base: "))
        porcentagem = float(input("Digite a porcentagem de decrescimo: "))
        print(moeda.diminuir(valor, porcentagem))
    else:
        print("Opção inválida!")
    sleep(5)
