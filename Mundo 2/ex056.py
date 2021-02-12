# Desafio 56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media_idade = 0
maioridade_homem = 0
mulheres_soma = 0
nome_maisvelho = ''
somaidade = 0

for contador in range(1, 5):
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [ M / F ]: ")).strip().upper()
    somaidade += idade
    if contador == 1 and sexo in "Mm":
        nome_maisvelho = nome
        maioridade_homem = idade
    if sexo in "Mm" and idade > maioridade_homem:
        nome_maisvelho = nome
        maioridade_homem = idade
    if sexo in "Ff" and idade < 20:
        mulheres_soma += 1
media_idade = somaidade / 4
print(f"A média de idade do grupo é {media_idade}\nO homem mais velho é o {nome_maisvelho} com {maioridade_homem}\nNesse grupo {mulheres_soma} mulheres tem menos de 20 anos")
