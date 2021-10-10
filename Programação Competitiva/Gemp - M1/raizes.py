a = int(input())
v = list(map(float, input().split()))

for e in v:
    e = e**(1/2)
    print(f"{e:.4f}")
