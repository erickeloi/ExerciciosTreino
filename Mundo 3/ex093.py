# Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

contador = 0

jogador_info = dict()
gols_por_partida = list()

nome = str(input("Digite aqui o nome do jogador: "))
partidas = int(input("Quantas partidas ele jogou: "))

jogador_info['nome'] = nome
jogador_info['partidas'] = partidas

while contador != partidas:
    gols = int(input(f"Quantos gols {nome} marcou no jogo nº{contador+1}: "))
    gols_por_partida.append(gols)
    contador += 1

jogador_info['gols por partida'] = gols_por_partida

print(f"Informações do jogador:\n\nnome: {jogador_info['nome']}, partidas: {jogador_info['partidas']}")
print("gols: ")
for indice, gols in enumerate(jogador_info['gols por partida']):
    print(f"Na {indice + 1}° partida: {gols} gols")

