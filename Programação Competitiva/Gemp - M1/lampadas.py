a = int(input())
b = str(input())
b = b.split()

l1 = 0
l2 = 0

for num in b:
    if int(num) == 1:
        if l1 == 0:
            l1 = 1
        else:
            l1 = 0
    else:
        if l1 == 0:
            l1 = 1
        else:
            l1 = 0

        if l2 == 0:
            l2 = 1
        else:
            l2 = 0

print(l1)
print(l2)

