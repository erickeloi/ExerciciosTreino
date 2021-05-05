# Exercício Python 079:
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores_numericos = list()
numero_digitado = int
continuar = 'S'
while continuar != "N":

    numero_digitado = int(input("Digite um número: "))

    if numero_digitado not in valores_numericos:
        valores_numericos.append(numero_digitado)
        print(f"O Número {numero_digitado} foi computado! ")
        valores_numericos.sort()
    else:
        print("Número Repetido!, não computado!")

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    while continuar not in "SN":
        print("Opção Inválida,")
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    if continuar == 'N':
        break

print(f"Os valores digitados, em ordem crescente, foram: {valores_numericos}")
