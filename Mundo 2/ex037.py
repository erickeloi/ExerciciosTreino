# Desafio 37
# Programa conversor de bases numéricas

# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
decision = int(input("Digite [ 1 ] para converter para Binário, \n"
                     "Digite [ 2 ] para converter para Octal, \n"
                     "Digite [ 3 ] para converter para Hexadecimal.\n"
                     "Sua Opção: "))
if decision == 1:
    print(f" {num} Convertido para Binário é {bin(num)[2:]}")
elif decision == 2:
    print(f" {num} Convertido para Octal é {oct(num)[2:]}")
elif decision == 3:
    print(f" {num} Convertido para Hexadecimal é {hex(num)[2:]}")
else:
    print("Digite uma opção válida.")
