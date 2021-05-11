# Exercício Python 091: 
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# Resolução um tanto confusa do guanabara com um novo modulo, uso do itemgetter.

from random import randint
from operator import itemgetter

jogadores = dict()

print("Valores sorteados: \n")
for contador in range(4):
    jogada = randint(1, 6)
    jogadores[f"jogador {contador + 1}"] = jogada

    print(f"O jogador {contador + 1} tirou {jogada} pontos no dado.")

print("\nRanking dos jogadores:")

lista_jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for indice, jogador in enumerate(lista_jogadores):
    print(
        f"{indice + 1}º lugar: {lista_jogadores[indice][0]} com {lista_jogadores[indice][1]} pontos")
