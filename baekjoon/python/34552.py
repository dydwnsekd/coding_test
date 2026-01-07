import sys

result = 0
m_list = list(map(int, sys.stdin.readline().strip().split()))
n = int(sys.stdin.readline())

for i in range(n):
    b, l, s = map(float, sys.stdin.readline().strip().split())

    if l >= 2.0 and s >= 17:
        result += m_list[int(b)]

print(result)

