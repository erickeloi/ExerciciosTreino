a = str(input())
a = a.split()

for i in range(0, len(a)):
    a[i] = int(a[i])

if a[0] == 0:
    print("C")
elif a[1] == 0:
    print("B")
elif a[1] == 1:
    print("A")
