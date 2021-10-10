a = str(input())
a = a.split()

for i in range(0, 4):
    a[i] = int(a[i])

if a[0] * a[1] == a[2] * a[3]:
    print("0")
elif a[0] * a[1] > a[2] * a[3]:
    print("-1")
else:
    print("1")
