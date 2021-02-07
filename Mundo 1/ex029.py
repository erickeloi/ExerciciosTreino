# Desafio 29
# lê a velocidade de um carro e se ele ultrapassar 80km/h ele é multado, a multa custa 7R$ por cada km acima do limite
vel = float(input("Digite aqui a velocidade do carro em Km/h: "))
if vel > 80:
    print("Você foi multado, pois ultrapassou o limite de 80Km/h.")
    print(f"Velocidade do Carro: {vel}, multa a pagar: {7*(vel - 80)}, pois está {vel - 80}Km/h acima do limite.")
else:
    print("Está dentro da velocidade permitida! Tudo certo! ")
