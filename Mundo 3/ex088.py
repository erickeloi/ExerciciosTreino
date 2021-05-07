# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

contador = 0
mega_sena = list()
lista_complementar = list()

numero_de_sorteios = int(input("Digite o número de sorteios: "))

print(f"Sorteando {numero_de_sorteios} jogos")

while contador != numero_de_sorteios:
    while True:
        palpite = randint(1, 60)
        if palpite not in lista_complementar:
            lista_complementar.append(palpite)
        if len(lista_complementar) == 6:
            break

    mega_sena.append(lista_complementar[:])
    lista_complementar.clear()
    contador += 1

print("Gerando Resultado...")

for num_do_sorteio, jogo in enumerate(mega_sena):
    print(f"jogo {num_do_sorteio}: {jogo}")
    sleep(0.5)
    
print("Fim do sorteio!")

