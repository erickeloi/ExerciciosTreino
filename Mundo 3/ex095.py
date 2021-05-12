# Exercício Python 095:
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista_jogadores = list()
lista_provisoria = list()
jogador_info = dict()
total_de_gols = 0

while True:
    jogador_info['nome'] = str(input("Digite o nome do jogador: "))
    partidas = int(input(f"Quantas partidas o {jogador_info['nome']} jogou: "))
    jogador_info['partidas'] = partidas

    for contador_provisorio in range(0, partidas):
        gols = int(input(f"Quantos gols o {jogador_info['nome']} fez na {contador_provisorio+1}° partida: "))
        lista_provisoria.append(gols)
        total_de_gols += gols

    jogador_info['gols'] = lista_provisoria[:]
    jogador_info['total de gols'] = total_de_gols

    lista_jogadores.append(jogador_info.copy())

    lista_provisoria.clear()
    total_de_gols = 0

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input("Opção Inválida!,\nQuer continuar? [S/N]: ")).strip().upper()[0]
    if continuar == 'N':
        break

print('---' * 20)
print(f'{"Nº":<4} {"Nome":<10} {"Partidas":>12} {"Total de Gols":>14}')
print('---' * 20)

for indice, jogador in enumerate(lista_jogadores):
    print(f'{indice:<4} {jogador["nome"]:<10} {jogador["partidas"]:>11} {jogador["total de gols"]:>13}')

while True:
    option = int(input("\nMostrar dados de qual jogador? (999 interrompe o programa): "))

    if option <= len(lista_jogadores):
        print()
        print(f"Jogador Nº{option}:")
        print(f"Nome: {lista_jogadores[option]['nome']}")
        print(f"Partidas Jogadas: {lista_jogadores[option]['partidas']}")
        print()
        for indice, gols in enumerate(lista_jogadores[option]['gols']):
            print(f"Na partida {indice+1}: {gols} gol(s) Marcados.")

    if option == 999:
        print(" Volte Sempre ")
        break


