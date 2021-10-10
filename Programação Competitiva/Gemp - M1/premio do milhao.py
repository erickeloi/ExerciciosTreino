a = int(input())

tot = int()
t = list()
for i in range(0, a):
    tot += int(input())
    if tot >= 1000000:
        t.append(i+1)

print(t[0])
