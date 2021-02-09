# Desafio 54
# Programa que lê 7 datas de nascimento e verifica quantas atingiram a maioridade (21 anos para cima)
from time import localtime
soma = 0
ano_atual = int(localtime()[0])
for contador in range(1, 8):
    data_nascimento = int(input(f"Digite a data de nascimento do indivíduo número {contador}: "))
    print("Anotado!")
    if (ano_atual - data_nascimento) >= 21:
        soma = soma + 1
print(f"Então, dentre esses {contador} indivíduos, {soma} são maiores de idade (21 anos)!")
