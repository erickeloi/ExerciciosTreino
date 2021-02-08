# Desafio 39
# Programa verificação de alistamento
from time import localtime
year = int(localtime()[0])
data = int(input("Digite sua data de nascimento: "))
idade = year - data
print(f"Então,você tem {idade} anos")
if idade == 18:
    print(f"E, está no momento certo para se alistar")
elif idade < 18:
    print(f"E, ainda falta {18 - idade} ano(s) para você se alistar")
    print(f"Ou seja, você vai se alistar no ano de {data + 18}")
elif idade > 18:
    print(f"E, seu alistamento deveria ter sido feito {idade - 18} ano(s) atrás, no ano de {data + 18}")
