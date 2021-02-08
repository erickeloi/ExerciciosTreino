# Desafio 38
# Lê 2 números inteiros e compara eles
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print(f"Então, o primeiro valor '{num1}' é maior que o segundo valor '{num2}'")
elif num2 > num1:
    print(f"Então, o segundo valor '{num2}' é maior que o primeiro valor '{num1}'")
elif num1 == num2:
    print(f"Os dois valores são iguais, ambos {num1}")
