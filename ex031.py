# Desafio 31
# lê a distância em Km e calcula o preço da passagem.
# (0,5R$ / Km) até 200Km e 0,45 para viagens mais longas.
distance = float(input("Digite aqui a distância a ser percorrida em Km: "))
if distance <= 200:
    print(f"Então, o preço da passagem é {distance * 0.5}R$")
else:
    print(f"Então, o preço da passagem é {distance * 0.45}R$")
