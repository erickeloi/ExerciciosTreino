# Exercício 68
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randrange
computador = randrange(1, 11)
contador = 0
print("Jogo Ímpar x Par")
while True:
    jogador = int(input("Digite seu número: "))
    escolha_jogador = str(input("Digite sua escolha [P/I]: ")).strip().upper()[0]
    if (computador + jogador) % 2 == 0 and escolha_jogador == "P":
        print("Você Ganhou!!!")
        print(f"O Computador escolheu o número \033[32m{computador}\033[m")
        contador += 1
        print(f"Iniciando Round {contador+1}!")
        computador = randrange(1, 11)
    elif (computador + jogador) % 2 != 0 and escolha_jogador == "I":
        print("Você Ganhou!!!")
        print(f"O Computador escolheu o número \033[32m{computador}\033[m")
        contador += 1
        print(f"Iniciando Round {contador+1}!")
        computador = randrange(1, 11)
    else:
        print("Você Perdeu!")
        print(f"O Computador escolheu o número \033[32m{computador}\033[m")
        if contador > 0:
            print(f"Você conseguiu \033[33m{contador}\033[m Vitória(s) seguida(s), parabéns!")
        break
print("Fim de jogo! Obrigado por jogar!")
