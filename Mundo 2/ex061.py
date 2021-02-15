# Desafio 61
# Refazer o desafio 51 usando a estrutura 'while' ao invés de 'for'

# Faça um programa de cálculo de uma PA e mostre os 10 primeiros termos

a1 = float(input("Digite o primeiro termo da progressão aritmética (P.A.): "))
r = float(input("Digite a razão dessa P.A.: "))
an = 0
contador = 0
while contador != 10:
    an = a1 + (contador * r)
    contador += 1
    print(f"{an} é o termo de número {contador}")
