# Exercício Python 115b: Arquivos com Python
# Vamos ver como fazer acesso a arquivos usando o Python.

from ex115.menu.menu import *
from time import sleep

arquivo_diretorio = "./banco_de_dados.txt"

while True:
    response = menu()
    if response == 1:
        try:
            with open(arquivo_diretorio, "r") as arquivo:
                for texto in arquivo:
                    print(texto, end='')
                sleep(5)
        except:
            print(f"Ainda Não existem pessoas cadastradas")

    elif response == 2:
        try:
            nome = str(input("Digite o nome da pessoa: "))
            idade = int(input("Digite a idade da pessoa (em anos): "))
            with open(arquivo_diretorio, 'a') as arquivo:
                arquivo.write(f"{nome},{idade}" + "\n")
            print("Cadastro Realizado com sucesso!")
        except:
            print("Erro, entrada inválida")
    elif response == 3:
        break
