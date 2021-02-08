# Desafio 41
# Lê idades e mostra sua categoria de natação
from time import localtime
year = int(localtime()[0])
useryear = int(input("Digite sua data de nascimento: "))
idade = year - useryear
if idade <= 9:
    print("Então você está na categoria MIRIM")
elif 10 <= idade <= 14:
    print("Então você está na categoria INFANTIL")
elif 15 <= idade <= 19:
    print("Então você está na categoria JUNIOR")
elif idade >= 20:
    print("Então você está na categoria SENIOR")
elif idade > 25:
    print("Então você está na categoria MASTER")
