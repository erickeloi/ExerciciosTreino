# Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from time import gmtime

ano_atual = gmtime()[0]
trabalhador = dict()
tempo_para_aposentadoria = 0

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ctps = int(input("Digite o número da sua carteira de trabalho ( Se não tiver, digite 0 ): "))

idade = ano_atual - ano_nascimento

trabalhador['nome'] = nome
trabalhador['idade'] = idade

if ctps != 0:
    trabalhador['Carteira de Trabalho'] = ctps
    ano_contratacao = int(input("Ano de contratação: "))
    salario = int(input("Qual seu salário: "))

    trabalhador['ano de contratação'] = ano_contratacao
    trabalhador['salario'] = salario

    aposentadoria = ano_contratacao + 35
    if aposentadoria - ano_atual >= 0:
        tempo_para_aposentadoria = aposentadoria - ano_atual
    else:
        tempo_para_aposentadoria = "Você já pode pedir sua aposentadoria, pois ja contribuiu mais de 35 anos."

else:
    trabalhador['Carteira de Trabalho'] = 'Não Possui'
    tempo_para_aposentadoria = "Ainda falta contrinbuir 35 anos para se aposentar"

print(f"Seus dados são: {trabalhador}\nInformações adicionais:\nTempo até a aposentadoria: {tempo_para_aposentadoria}")
