import sys

result = 0

m, dm = map(int, sys.stdin.readline().split())
h, dh = map(int, sys.stdin.readline().split())

cases = int(sys.stdin.readline())

for _ in range(cases):
    c, b = map(int, sys.stdin.readline().split())

    m_value = []
    h_value = []
    m_temp = m
    h_temp = h

    for i in range(c, 0, -1):
        m_value.append(m_temp)
        if m_temp < dm:
            m_temp = 0
        else:
            m_temp -= dm

    for i in range(b, 0, -1):
        h_value.append(h_temp)
        if h_temp < dh:
            h_temp = 0
        else:
            h_temp -= dh

    if sum(m_value) > sum(h_value):
        result += sum(m_value)
    else:
        result += sum(h_value)

print(result)
