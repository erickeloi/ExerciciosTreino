# Exercício Python 102: Função para Fatorial
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=True):
    fatorial = 1
    if show == False:
        for contador in range(numero, 0, -1):
            fatorial *= contador
        print(fatorial)
    elif show == True:
        for contador in range(numero, 0, -1):
            fatorial *= contador
            print(f"{contador} x ", end="")
        print(f"0! = {fatorial}")


numero = int(input("Digite um número: "))

show = str(input("Quer que o processo seja mostrado? [S/N]: ")).strip().upper()[0]
while show not in 'SN':
    show = str(input("Quer que o processo seja mostrado? [S/N]: "))
if show == 'N':
    show = False
elif show == 'S':
    show = True

fatorial(numero, show)
