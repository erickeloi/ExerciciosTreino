# Exercício Python 111: Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

def moeda(valor):
    return f"R${valor:.2f}"


def metade(numero, real=True):
    if real:
        return moeda(numero/2)
    elif not real:
        return numero / 2


def dobro(numero, real=True):
    if real:
        return moeda(numero * 2)
    elif not real:
        return numero * 2


def aumentar(valor, porcentagem, real=True):
    if real:
        return moeda(valor * (100 + porcentagem)/100)
    elif not real:
        return valor * (100 + porcentagem)/100


def diminuir(valor, porcentagem, real=True):
    if real:
        return moeda(valor * (100 - porcentagem)/100)
    elif not real:
        return valor * (100 - porcentagem)/100


def resumo(valor, porcentagem):
    print(f"""
    Resumo das operações:
    * Valor = R${valor}, Porcentagem = {porcentagem}%.\n
    Dobro = {dobro(valor)}
    Metade = {metade(valor)}\n
    Acrescimo (+ {porcentagem}%) = {aumentar(valor, porcentagem)}
    Decrescimo (- {porcentagem}%) = {diminuir(valor, porcentagem)}
""")
