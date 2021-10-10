a = str(input())
a = a.split()

for i in range(0, 2):
    a[i] = float(a[i])

r = (a[0] + a[1])/2

if  r >= 7:
    print("Aprovado")
elif 4 <= r < 7:
    print("Recuperacao")
else:
    print("Reprovado")
