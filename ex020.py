#Desafio 20
#Programa Sorteador de aluno, sorteia uma ordem de alunos
from random import shuffle
aluno1 = str(input("Digite aqui o nome de um dos alunos: "))
aluno2 = str(input("Digite aqui o nome de um aluno diferente do anterior: "))
aluno3 = str(input("Digite aqui o nome de um aluno, diferente dos anteriores: "))
aluno4 = str(input("Digite aqui o nome de um aluno, diferente dos anteriores: "))
aula = [aluno1,aluno2,aluno3,aluno4]
shuffle(aula)
print(aula)

