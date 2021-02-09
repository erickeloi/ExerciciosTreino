# Desafio 48
# Soma dos números ímpares multiplos de 3 entre 1 a 500
soma = 0
for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        print(num)
        soma += num
print(f"Então, a soma desses números acima é {soma}")
