# Exercício Python 112:
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from ex112.utilidadesCeV.moeda import moeda
from ex112.utilidadesCeV.dado import dado
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
        valor = dado.leiaDinheiro()
        print(f"O dobro de R${valor} é {moeda.dobro(valor)}")
    elif operacao == 2:
        valor = dado.leiaDinheiro()
        print(f"A metade de R${valor} é {moeda.metade(valor)}")
    elif operacao == 3:
        valor = dado.leiaDinheiro()
        porcentagem = float(input("Digite a porcentagem de acrescimo: "))
        print(f"O valor R${valor} tendo um acrescimento de {porcentagem}% é: {moeda.aumentar(valor, porcentagem)}")
    elif operacao == 4:
        valor = dado.leiaDinheiro()
        porcentagem = float(input("Digite a porcentagem de decrescimo: "))
        print(f"O valor R${valor} tendo um decrescimo de {porcentagem}% é: {moeda.diminuir(valor, porcentagem)}")
    elif operacao == 5:
        valor = dado.leiaDinheiro()
        porcentagem = float(input("Digite a porcentagem: "))
        moeda.resumo(valor, porcentagem)
    else:
        print("Opção inválida!")
    sleep(4)
