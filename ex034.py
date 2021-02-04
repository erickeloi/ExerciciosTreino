# Desafio 34
# Calcula o aumento de salário
salario = float(input("Digite aqui o seu salário atual: "))
if salario > 1250:
    print(f"Então, você terá um aumento de 10%, e seu salário final será: {salario * 1.1}R$")
    print(f"Ou seja, um aumento de {salario *0.1}R$")
else:
    print(f"Então, você terá um aumento de 15%, e seu salário final será: {salario * 1.15}R$")
    print(f"Ou seja, um aumento de {salario *0.15}R$")
