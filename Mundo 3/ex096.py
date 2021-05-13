# Exercício Python 096:
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(comprimento, largura):
    area = comprimento * largura
    print(f"O terreno de dimensões: {comprimento}m x {largura}m tem área de {area}m²")


comprimento = int(input("Digite o Comprimento do terreno (em metros): "))
largura = int(input("Digite a Largura do terreno (em metros): "))
area(comprimento, largura)

