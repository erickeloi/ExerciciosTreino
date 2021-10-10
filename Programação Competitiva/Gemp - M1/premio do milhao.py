a = int(input())

tot = int()
t = int()
for i in range(0, a):

    # Melhoramento para consumir menos memoria,
    # Em resumo, quando o total já é maior que 1 milhão, ele para de acumular o total.
    # Porém, no neps ele da um erro de compilação, visto que o python testado é o 3.7 e esse é o 3.9
    if tot <= 1000000:
        tot += int(input())
        if tot >= 1000000:
            t = i+1
    else:
        b = str(input())

print(t)
