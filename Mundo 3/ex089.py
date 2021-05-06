# Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# (Não consegui fazer a consulta individual de cada um, mas mostrei todos no final)

lista_nome = list()
lista_notas = list()
alunos_info = list()
media_dos_alunos = list()

while True:
    nome = str(input("Digite o nome do aluno: "))
    lista_nome.append(nome)

    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    lista_notas.append(nota1)
    lista_notas.append(nota2)

    lista_nome.append(lista_notas[:])

    alunos_info.append(lista_nome[:])

    lista_nome.clear()
    lista_notas.clear()

    continuar = str(input("Quer Continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Opção inválida!\nQuer Continuar? [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        break

print("Gerando Boletim...")

for contador, aluno in enumerate(alunos_info):

    nota_media = (aluno[1][0]+aluno[1][1])/2
    nome_do_aluno = aluno[0]

    print(f"A média do aluno {nome_do_aluno} é {nota_media}")

print(f"A lista de Boletim escolar é: {alunos_info}")
