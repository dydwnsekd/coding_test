import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    s, i, j = sys.stdin.readline().strip().split()
    i = int(i)
    j = int(j)

    print(s[:i]+s[j:])

