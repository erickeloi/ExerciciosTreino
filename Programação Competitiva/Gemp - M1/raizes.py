input()
v = list(map(float, input().split()))

for e in v:
    print(f"{e**(1/2):.4f}")
