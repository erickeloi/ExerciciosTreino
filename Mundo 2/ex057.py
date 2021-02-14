# Desafio 57
# Programa que lê o sexo de uma pessoa [M] / [F]. Caso não for um valor válido peça a digitação novamente desse valor.
sexo = ""
while "Feminino" != sexo != "Masculino":
    sexo = str(input("Sexo [M] / [F]: ")).strip().upper()
    if "F" != sexo != "M":
            print("Digite uma opção válida!")
    elif sexo == "M":
            sexo = "Masculino"
    elif sexo == "F":
            sexo = "Feminino"
print(f"Então, seu sexo é {sexo}")
