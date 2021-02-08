# Desafio 43
# Calculadora de IMC, COMPLETO!
peso = float(input("Digite aqui seu peso em Kg: "))
altura = float(input("Digite aqui sua altura em metros: "))
imc = round((peso / altura**2), 1)
if imc < 10:
    print("Então, você apresenta Desnutrição Grau V")
elif 10.0 <= imc <= 12.9:
    print("Então, você apresenta Desnutrição Grau IV")
elif 13 <= imc <= 15.9:
    print("Então, você apresenta Desnutrição Grau III")
elif 16 <= imc <= 16.9:
    print("Então, você apresenta Desnutrição Grau II")
elif 17 <= imc <= 18.4:
    print("Então, você apresenta Desnutrição Grau I")
elif 18.5 <= imc <= 24.9:
    print("Então, você apresenta um IMC normal! ")
elif 25 <= imc <= 29.9:
    print("Então, você apresenta Pré-Obesidade")
elif 30 <= imc <= 34.9:
    print("Então, você apresenta Obesidade Grau I")
elif 35 <= imc <= 39.9:
    print("Então, você apresenta Obesidade Grau II")
elif imc > 40:
    print("Então, você apresenta Obesidade Grau III")
print(f"Seu IMC é {imc}, com taxa de erro de até 0.10 +-")
