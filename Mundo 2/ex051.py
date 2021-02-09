# Desafio 51
# Faça um programa de cálculo de uma PA e mostre os 10 primeiros termos
a1 = float(input("Digite o primeiro termo da progressão aritmética (P.A.): "))
r = float(input("Digite a razão dessa P.A.: "))
an = 0
for contador in range(0, 10):
    an = a1 + (contador * r)
    print(f"{an} é o termo de número {contador+1}")
