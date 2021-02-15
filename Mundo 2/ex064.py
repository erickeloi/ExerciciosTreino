# Desafio 64
# Lê vários números inteiros e vai somando eles, até o usuário digitar a condição de parada ''999''
numeros = 0
contador = 0
soma = 0
while numeros != 999:
    numeros = int(input("Digite um número inteiro para contabilizar ou '999' para terminar o programa: "))
    if numeros != 999:
        contador += 1
        soma = soma + numeros
    else:
        print("Programa Encerrado! ")

print(f" Você digitou \033[33m{contador}\033[m números e a soma deles deu \033[34m{soma}\033[m")
