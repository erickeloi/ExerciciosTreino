#Desafio 11
#Programa Tinta para a parede
#Lê a altura e comprimento de uma parede, calcula sua área e a quantidade de tinta necessária para pintá-la. 1L tinta = 2m2.
altura = float(input("Digite a altura da parede, em metros: "))
comprimento = float(input("Digite o comprimento da parede, em metros: "))
area = altura*comprimento
litros = area/2
print(f"A parede possui área de {area} metros quadrado\nE, portanto, precisa de {litros} litros de tinta para ser pintada por completo")
