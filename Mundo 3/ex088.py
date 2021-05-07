# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

sorteio = contador = 0
mega_sena = list()

numero_de_sorteios = int(input("Digite o número de sorteios: "))

print(f"Sorteando {numero_de_sorteios} jogos")

while sorteio != numero_de_sorteios:
    
    while sorteio != numero_de_sorteios:
        
        palpite = randint(1, 60)
        if palpite not in mega_sena:
            mega_sena.append(palpite)
            contador += 1
        if contador >= 6:
            contador = 0
            break

    print(f"Jogo {sorteio+1}: {mega_sena}")
    
    mega_sena.clear()
    sorteio += 1
    sleep(1)
    
print("Fim do sorteio!")
