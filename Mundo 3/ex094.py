# Exercício Python 094:
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista_de_pessoas = list()
lista_mulheres = list()
lista_pessoas_idade = list()
pessoas_info = dict()
contador_pessoas = idades = 0


while True:
    pessoas_info['nome'] = str(input("Nome: "))

    pessoas_info['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while pessoas_info['sexo'] not in 'MF':
        pessoas_info['sexo'] = str(input("Opção Inválida !,\nSexo [M/F]: ")).strip().upper()[0]

    pessoas_info['idade'] = int(input("Idade: "))

    lista_de_pessoas.append(pessoas_info.copy())

    idades += pessoas_info['idade']
    contador_pessoas += 1

    pessoas_info.clear()

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input("Opção Inválida !,\nQuer continuar? [S/N]: ")).strip().upper()[0]
    if continuar == 'N':
        break


media_idades = idades/contador_pessoas

for pessoa in lista_de_pessoas:
    if pessoa['sexo'] == 'F':
        lista_mulheres.append(pessoa.copy())

for pessoa in lista_de_pessoas:
    if pessoa['idade'] > media_idades:
        lista_pessoas_idade.append(pessoa.copy())


print()
print(f"foram cadastradas: {contador_pessoas} pessoas")
print(f"A média de idade foi {media_idades} anos")
print()

if len(lista_mulheres) > 0:
    print("Mulheres cadastradas: ")
    for indice, mulheres in enumerate(lista_mulheres):
        print(f"nome: {lista_mulheres[indice]['nome']}, idade: {lista_mulheres[indice]['idade']}, ")
else:
    print("Sem mulheres cadastradas")

print()

print("Pessoas com idade acima da média: ")
for indice, pessoa in enumerate(lista_pessoas_idade):
    print(f"nome: {pessoa['nome']}, idade: {pessoa['idade']}, sexo: {pessoa['sexo']}")
