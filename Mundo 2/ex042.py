# Desafio 42
# lê o valor de 3 retas e responde se elas podem formar um triângulo
reta1 = float(input("Digite aqui o valor da primeira reta: "))
reta2 = float(input("Digite aqui o valor da segunda reta: "))
reta3 = float(input("Digite aqui o valor da terceira reta: "))
if (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2 and (reta1 + reta2) > reta3:
    print("Dá para formar um triângulo")
    if reta1 == reta2 == reta3:
        print(f"E, ele é um triângulo equilátero, pois possui todos os lados iguais de {reta1}")
    elif reta1 != reta2 and reta1!= reta3 and reta2 != reta3:
        print("E, ele é um triângulo escaleno, pois possui todos os lados diferentes.")
    elif (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1):
        print("E, ele é um triângulo Isósceles, pois possui dois lados iguais.")
else:
    print("Não dá para formar um triângulo")
