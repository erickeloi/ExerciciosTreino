# Exercício 69
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos
contador_maioridade = contador_homem = contador_mulher_20 = idade = 0
sexo = " "
continuar = " "
while True:
    print("-----Cadastre uma pessoa-----")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while sexo not in "MmFf":
        print("Digite uma opção válida [M/F]")
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    print("-----------------------------")
    if idade > 18:
        contador_maioridade += 1
    if sexo == "M":
        contador_homem += 1
    if sexo == "F" and idade < 20:
        contador_mulher_20 += 1
    continuar = str(input("Quer Cadastrar mais uma pessoa? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        print("Digite uma opção válida '[S/N]'")
        continuar = str(input("Quer Cadastrar mais uma pessoa? [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        break
print("Fim dos Cadastros")
print(f"O número de pessoas maiores de 18 anos foi: {contador_maioridade}")
print(f"O número de homens foi {contador_homem}")
print(f"O número de mulheres com menos de 20 anos foi: {contador_mulher_20}")
