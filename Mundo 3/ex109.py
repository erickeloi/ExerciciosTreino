# Exercício Python 109: Formatando Moedas em Python
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from ex109 import moeda
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
        print(f"O dobro de R${valor} é {moeda.dobro(valor)}")
    elif operacao == 2:
        valor = float(input("Digite um valor para ser reduzido a metade: R$"))
        print(f"A metade de R${valor} é {moeda.metade(valor)}")
    elif operacao == 3:
        valor = float(input("Digite o valor base: R$"))
        porcentagem = float(input("Digite a porcentagem de acrescimo: "))
        print(f"O valor R${valor} tendo um acrescimento de {porcentagem}% é: {moeda.aumentar(valor, porcentagem)}")
    elif operacao == 4:
        valor = float(input("Digite o valor base: R$"))
        porcentagem = float(input("Digite a porcentagem de decrescimo: "))
        print(f"O valor R${valor} tendo um decrescimo de {porcentagem}% é: {moeda.diminuir(valor, porcentagem)}")

    else:
        print("Opção inválida!")
    sleep(4)
