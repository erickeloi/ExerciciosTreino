# Desafio 58
# Melhoria no " JOGO DA ADVINHAÇÃO " do exercício 28
import random
num = random.randrange(0, 11)
contador = 0
advinha = 11
while 69 != num != advinha:
    advinha = int(input("Advinhe que número eu estou pensando, é de 0 a 10: "))
    contador += 1
    if num == advinha:
        print("Acertou!!!")
        if contador == 1:
            print("Ganhou de primeira!!!, Parabéns!!!")
            print(f"Pensei no número {num} mesmo")
    elif num != advinha:
        print("Tente Novamente!, sua cabeça é tão grande que parece a do MegaMente!!!")
        print(f"Você já tentou {contador} vezes")
        print(f"Digite '69' para desistir.")
print("Fim de Jogo")
print(f"O número que eu pensei foi o \033[33m'{num}'\033[m")
print(f"Você tentou \033[31m{contador}\033[m vezes")
