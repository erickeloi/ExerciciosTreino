# Desafio 59
# lê dos valores e mostra um menu para realizar operações com operadores aritimeticos:
# Obs: quando eu aprender a definir funções, vai ser mais conveniente ao invés de repetir a opção de continuar repetida vezes...
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
option = 100
continuar = []
while option != 99:
    option = int(input(
'''[ 1 ] Somar 
[ 2 ] Subtrair
[ 3 ] Multiplicar 
[ 4 ] Dividir 
[ 5 ] Qual Maior Número?
[ 6 ] Novos Números 
[ 10 ] All in One
[ 99 ] Sair do Programa
Digite sua Opção: '''))
    if option == 1:
        print(f" {num1} + {num2} = {num1+num2}")
        continuar = input("Aperte enter ou digite qualquer coisa para continuar: ")

    elif option == 2:
        print(f" {num1} - {num2} = {num1 - num2}")
        print(f" {num2} - {num1} = {num2 - num1}")
        continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))

    elif option == 3:
        print(f" {num1} * {num2} = {num1*num2}")
        print("'A ordem dos tratores não altera o viaduto'")
        continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))


    elif option == 4:
        print(f" {num1} / {num2} = {num1/num2}")
        print(f" {num2} / {num1} = {num2/num1}")
        continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))

    elif option == 5:
        if num1 > num2:
            print(f" {num1} > {num2}")
            continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))
        elif num1 == num2:
            print(f" {num1} = {num2}")
            continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))
        else:
            print(f" {num1} < {num2}")
            continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))

    elif option == 6:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))

    elif option == 10:
        print("ALL IN ONE!\n")

        print(f"Soma: {num1} + {num2} = {num1+num2}\n")

        print(f"Subtração 1: {num1} - {num2} = {num1 - num2}")
        print(f"Subtração 2: {num2} - {num1} = {num2 - num1}\n")

        print(f"Multiplicação: {num1} * {num2} = {num1*num2}\n")

        print(f"Divisão: {num1} / {num2} = {num1/num2}")
        print(f"Divisão: {num2} / {num1} = {num2/num1}\n")

        if num1 > num2:
            print(f" {num1} > {num2}")
        elif num1 == num2:
            print(f"Igual! {num1} = {num2}")
        else:
            print(f" {num1} < {num2}")

        print("\nAll IN ONE!")
        continuar = print(input("Aperte enter ou digite qualquer coisa para continuar: "))
    else:
        print("Digite uma opção válida: ")

print("Fim")
