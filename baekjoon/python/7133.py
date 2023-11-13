import sys

result = 0

m, dm = map(int, sys.stdin.readline().split())
h, dh = map(int, sys.stdin.readline().split())

cases = int(sys.stdin.readline())

for _ in range(cases):
    c, b = map(int, sys.stdin.readline().split())

    m_value = []
    h_value = []

    for i in range(c, 0, -1):
        m_value.append(m)
        if m < dm:
            m = 0
        else:
            m -= dm

    for i in range(b, 0, -1):
        h_value.append(h)
        if h < dh:
            h = 0
        else:
            h -= dh

    if sum(m_value) > sum(h_value):
        result += sum(m_value)
    else:
        result += sum(h_value)

print(result)



