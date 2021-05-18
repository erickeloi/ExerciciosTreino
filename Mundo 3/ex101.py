# Exercício Python 101:
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from time import gmtime
ano_atual: int = gmtime()[0]


def voto(ano_de_nascimento: int):
    idade: int = ano_atual - ano_de_nascimento

    if idade < 16:
        return "Não vota"
    elif 18 <= idade <= 64:
        return "Obrigatório"
    elif 16 <= idade <= 17 or idade >= 65:
        return "Opcional"


ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
resultado = voto(ano_de_nascimento)

print(f"Com idade '{ano_atual - ano_de_nascimento} anos' tem voto: {resultado}")

