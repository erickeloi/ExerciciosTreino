# Exercício Python 115: Crie um pequeno sistema modularizado
# Crie um Pequeno sistema Modularizado
# que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistemas terá 3 opções:
# Listar, Cadastrar, Sair

from ex115.menu.menu import *
from time import sleep

arquivo_diretorio = "./banco_de_dados.txt"

while True:
    response = menu()
    if response == 1:
        try:
            with open(arquivo_diretorio, "r") as arquivo:
                for linha in arquivo:
                    informacao = linha.split(",")
                    informacao[1] = informacao[1].replace("\n", "")
                    print(f"{informacao[0]:<30} Idade: {informacao[1]:>3} anos")

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
