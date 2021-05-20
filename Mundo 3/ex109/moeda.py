# Exercício Python 109:
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

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
