# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

numero_de_sorteios = int(input("Digite o número de sorteios: "))
sorteio = 0
print(f"Sorteando {numero_de_sorteios} jogos")

while sorteio != numero_de_sorteios:
    mega_sena = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f"Jogo {sorteio+1}: {mega_sena}")
    sorteio += 1
    sleep(1)

print("Fim do sorteio!")

