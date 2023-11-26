import sys

s = list(sys.stdin.readline().strip())
cases = int(sys.stdin.readline())

for _ in range(cases):
    n1, n2 = map(int, sys.stdin.readline().split())

    temp = s[n1]
    s[n1] = s[n2]
    s[n2] = temp

print("".join(s))
