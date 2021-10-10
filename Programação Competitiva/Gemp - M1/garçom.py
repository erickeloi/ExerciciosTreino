a = int(input())

tot_q: int() = 0

for i in range(0, a):
    b = str(input())
    b = b.split()
    if int(b[0]) > int(b[1]):
        tot_q += int(b[1])

print(tot_q)
