# Desafio 36
# Programa comprador de casa
casa = float(input("Digite o valor da casa selecionada: "))
salario = float(input("Digite o valor do seu salário: "))
anos = int(input("Digite em quantos anos você pretende pagar toda a casa: "))
meses = anos * 12
if casa / meses > 0.3 * salario:
    print(f"Para pagar uma casa de {casa}R$ em {anos} anos,\n"
          f"as parcelas seriam de {casa/meses:.3f}R$ ")
    print("Emprestimo negado.")
else:
    print("Emprestimo aprovado!")
    print(f"Você irá pagar {casa / meses:.3f}R$ mensalmente por {anos} anos até quitar o móvel.")
