# Exercício Python 115a: Criando um menu em Python
# Vamos criar um menu em Python, usando modularização.

def options_list():
    print("-" * 45)
    print(f"\033[1;33m 1 -\033[1;35m Ver pessoas cadastradas \033[m")
    print(f"\033[1;33m 2 -\033[1;35m Cadastrar nova pessoa \033[m")
    print(f"\033[1;33m 3 -\033[1;35m Sair do Sistema \033[m")
    print("-" * 45)


def options_value():
    while True:
        try:
            option = int(input("\033[1;33mDigite sua opção:\033[m "))
            if option in range(1, 4):
                break
            else:
                print("Opção inexistente")
        except:
            print("Valor de opção inválido!")
            options_list()

    if option == 3:
        print("-" * 45)
        print("Volte Sempre, Obrigado!")
        print("-" * 45)

    return option


def menu():
    print("-" * 45)
    print("Menu Principal".center(45))

    options_list()
    option = options_value()

    return option
