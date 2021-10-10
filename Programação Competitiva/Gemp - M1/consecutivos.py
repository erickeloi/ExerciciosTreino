a = int(input())
v = list(map(int, input().split()))

m_aux: int() = 1
m: int() = 1
c: int() = 0

for e in v:
    if c > 0:
        if e == ult:
            m_aux += 1
            if m_aux > m:
                m = m_aux
        else:
            m_aux = 1

        ult = e
    else:
        ult = e
        c += 1

print(m)
