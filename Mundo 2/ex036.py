# Desafio 36
# Programa comprador de casa
casa = float(input("Digite o valor da casa selecionada: "))
salario = float(input("Digite o valor do seu salário: "))
tempo = int(input("Digite em quantos anos você pretende pagar toda a casa: "))
if casa / tempo > 0.3 * salario:
    print("Emprestimo negado.")
else:
    print("Emprestimo aprovado!")
    print(f"Você irá pagar {(casa / tempo)}R$ mensalmente por {tempo} anos até quitar o móvel.")