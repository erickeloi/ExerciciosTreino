# Desafio 50
# Lê 6 numeros inteiros, desconsidera os impares e soma os pares.
num = 0
soma = 0
for contador in range(1, 7):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma += num
print(f"Então, a soma dos números pares é {soma}")
