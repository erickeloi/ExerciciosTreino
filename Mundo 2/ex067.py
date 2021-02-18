# Exercício 67
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print("Programa Tabuada de números inteiros 'X'")
while True:
    tabuada = int(input("Digite um número: "))
    if tabuada < 0:
        break
    else:
        for contador in range (1, 11):
            print(f"{tabuada} x {contador} = {tabuada * contador}")
        print("\nPara parar digite um número negativo!")
print("Fim do programa Tabuada 3.0")
