# Exercício Python 110: Reduzindo ainda mais seu programa
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

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
