# Exercício Python 105: Analisando e gerando Dicionários
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(notas, situacao=True):
    """
        -> Recebe várias notas de uma turma, faz uma análise dessas informações e retorna um Dicionário com elas.

        :param notas: (Obrigatório) Várias Notas de alunos podem ser digitadas para a análise

        :param situacao: (Opcional) True ou False, False por padrão
        você escolhe se deseja que o dicionário contenha a análise subjetiva da turma

        :return: Retorna um Dicionário com as informações:
        - Maior Nota
        - Menor Nota
        - Média da Turma
        - A Situação da Turma (Opcional): Ruim, Regular, Boa
        """

    dicionario_de_alunos = dict()
    sit = ""
    maior = menor = media = total = 0

    for contador, nota in enumerate(notas):
        if contador == 0:
            menor = nota
            maior = nota
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        total += nota

    media = total / len(notas)

    dicionario_de_alunos = {
        "Quantidade de Notas": len(notas),
        "Maior Nota": maior,
        "Menor Nota": menor,
        "Média da Turma": media
    }

    if media >= 7:
        sit = "Boa"
    elif 5 <= media < 7:
        sit = "Regular"
    elif media < 5:
        sit = "Ruim"

    if situacao == False:
        return dicionario_de_alunos

    if situacao == True:
        dicionario_de_alunos["Situação"] = sit
        return dicionario_de_alunos


notas_alunos = list()

while True:
    numero = float(input("Digite as notas dos alunos (999 para parar): "))
    if numero == 999:
        break
    notas_alunos.append(numero)

print(notas(notas_alunos, situacao=True))
