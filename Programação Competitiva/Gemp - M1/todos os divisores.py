a = int(input())

for i in range(1, a):
    if a % i == 0:
        print(i, end=" ")
print(a)
