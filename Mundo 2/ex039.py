# Desafio 39
# Programa verificação de alistamento
from time import localtime
year = int(localtime()[0])
data = int(input("Digite sua data de nascimento: "))
idade = year - data
if idade == 18:
    print(f"Então você tem {idade} anos e está no momento certo para se alistar")
elif idade < 18:
    print(f"Então ainda falta {18 - idade} anos para você se alistar")
elif idade > 18:
    print(f"Então seu alistamento deveria ter sido feito {idade - 18} anos atrás")
