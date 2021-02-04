# Desafio 32
# lê um ano e diz se esse ano é um ano bissexto
ano = int(input("Digite aqui o ano para saber se ele é bissexto ou não: "))
if ano % 4 == 0:
    print("Esse é um ano bissexto")
else:
    print("Esse não é um ano bissexto")
