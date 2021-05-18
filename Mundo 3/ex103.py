# Exercício Python 103: Ficha do jogador
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# O nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<Desconhecido>', gols=0):
    print()
    print(f"O jogador {jogador} marcou {gols} gol(s) no campeonato")


nome_jogador = str(input("Nome do jogador: "))
if nome_jogador == "":
    nome_jogador = "<Desconhecido>"

n_gols = str(input("Número de gol(s): "))
if n_gols.isnumeric():
    n_gols = int(n_gols)
elif n_gols == "":
    n_gols = 0
elif n_gols.isalnum():
    n_gols = 0


ficha(nome_jogador, n_gols)
