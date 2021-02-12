# Desafio 54
# Programa que lê 7 datas de nascimento e verifica quantas atingiram a maioridade (21 anos para cima)
from time import localtime
soma_maior = 0
soma_menor = 0
ano_atual = int(localtime()[0])
for contador in range(1, 8):
    data_nascimento = int(input(f"Digite a data de nascimento do indivíduo número {contador}: "))
    print("Anotado!")
    if (ano_atual - data_nascimento) >= 21:
        soma_maior = soma_maior + 1
    else:
        soma_menor = soma_menor + 1
print(f"Então, dentre esses {contador} indivíduos, {soma_maior} são maiores de idade (>21 anos)!\nE {soma_menor} indivíduos são menores de idade (<21 anos)")
