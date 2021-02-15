# Desafio 62
# Refazer o desafio 51 usando a estrutura 'while' ao invés de 'for' e coloque a opção de mais termos.

a1 = 0
r = 0
option = 1
an = 0
contador = 0

while option != 0:

    a1 = float(input("Digite o primeiro termo da progressão aritmética (P.A.): "))
    r = float(input("Digite a razão dessa P.A.: "))
    option = int(input("Digite quantos termos da P.A. o programa deve cálcular: "))

    while contador != option:
        an = a1 + (contador * r)
        contador += 1
        print(f"{an} é o termo de número {contador}")

    option = int(input("Digite '0' para terminar, ou qualquer outro número para continuar: "))

print("Fim")
