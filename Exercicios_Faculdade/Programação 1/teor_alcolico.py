# 1 oz = 29.57mL
# 1lbs = 0.45kg
sexo = str(input("Digite seu sexo [F ou M]: "))[0].upper()

total_de_alcool = float(input("Digite o total de bebida consumida (em ml): "))
teor = float(input("Digite o teor de alcool da bebida (Em porcentagem): "))

A = total_de_alcool * (teor/100)
A = A/29.57

W = float(input("Digite seu peso (em kg): "))
W = W/0.45

razao = float()

if sexo == "M":
    razao = 0.73
if sexo == "F":
    razao = 0.66

H = float(input("Digite quantas horas se passaram desde o seu ultimo drink: "))

BAC = ((A * 5.14 / (W * razao)) - 0.015 * H)

print(f"Seu BAC é {BAC:.2f}")
if BAC > 0.08:
    print("Você não está autorizado a dirigir")
    while BAC > 0.08:
        H_novo = int(H) + 1
        
        
        
else:
    print("Pode dirigir")
