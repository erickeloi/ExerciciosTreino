# Exercício Python 090:
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = {}
situacao = ''

aluno = str(input("Digite o Nome do aluno: "))
media = float(input(f"Digite a Média do {aluno}: "))

while media not in range(0, 11):
    media = float(input("Opção inválida,\nDigite a Média do aluno: "))

if 7 <= media <= 10:
    situacao = 'Aprovado'
elif media < 7:
    situacao = 'Reprovado'

boletim['Aluno'] = aluno
boletim['Média'] = media
boletim['Situacao'] = situacao

print("\nCalculando resultado...\n")

for key, values in boletim.items():
    print(f"{key}: {values}")
