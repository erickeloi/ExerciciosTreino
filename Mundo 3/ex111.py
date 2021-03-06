# Exercício Python 111: Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107, 108, 109 E 110 para o primeiro pacote e mantenha tudo funcionando.

from ex111.utilidadesCeV.moeda import moeda
from time import sleep

while True:
    print("""
    [ 1 ] - Dobrar
    [ 2 ] - Metade
    [ 3 ] - Aumentar
    [ 4 ] - Diminuir
    [ 5 ] - Resumo / Todas as Operações
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
    elif operacao == 5:
        valor = float(input("Digite o valor base: R$"))
        porcentagem = float(input("Digite a porcentagem: "))
        moeda.resumo(valor, porcentagem)
    else:
        print("Opção inválida!")
    sleep(4)
