# Desafio 45
# Jogo Jokênpo contra o Computador
from random import randrange
ia = randrange(1, 4)
print("""Jogue contra o Computador!!!
Pedra Papel Tesoura
  1     2      3""")
human = int(input("Digite sua opção: "))
if ia == 1 and human == 1:
    print("Empate!!!")
    print("Você e a Máquina escolheram Pedra!")
elif ia == 1 and human == 2:
    print("Você Ganhou!!!")
    print("A máquina escolheu Pedra e você escolheu Papel!")
elif ia == 1 and human == 3:
    print("Você Perdeu!!!")
    print("A máquina escolheu Pedra e você escolheu Tesoura!")
elif ia == 2 and human == 1:
    print("Você Perdeu!!!")
    print("A máquina escolheu Papel e você escolheu Pedra!")
elif ia == 2 and human == 2:
    print("Empatou!!!")
    print("Você e a máquina escolheram Papel!")
elif ia == 2 and human == 3:
    print("Você Ganhou!!!")
    print("A máquina escolheu Papel e você escolheu Tesoura!")
elif ia == 3 and human == 1:
    print("Você Ganhou!!!")
    print("A máquina escolheu Tesoura e você escolheu Pedra")
elif ia == 3 and human == 2:
    print("Você Perdeu!!!")
    print("A máquina escolheu Tesoura e você escolheu Papel!")
elif ia == 3 and human == 3:
    print("Empatou!!!")
    print("Você e a máquina escolheram Tesoura")
else:
    print("Digite uma opção válida! ")
