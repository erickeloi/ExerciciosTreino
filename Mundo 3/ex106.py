# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. I
# importante: use cores.
from time import sleep

while True:
    print("\033[44;97m-=" * 30)
    print(" " * 15, "Sistemas de Ajuda PyHelp")
    print("-=" * 30)

    comando = str(input(f"\033[mQual comando você deseja ajuda [ Digite: \033[4;31m'FIM'\033[m para Encerrar o programa ]: "))
    if comando == "FIM":
        break

    print(f"\033[47;97m", "-=" * 30)
    print(" " * 10, f"Acessando o Manual do comando '{comando}'")
    print(f"-=" * 30, "\n\033[m")

    help(comando)
    sleep(5)
