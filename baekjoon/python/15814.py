import sys

s = list(sys.stdin.readline().strip())
cases = int(sys.stdin.readline())

for _ in range(cases):
    n1, n2 = map(int, sys.stdin.readline().split())

    temp = s[n1+1]
    s[n1+1] = "a"
    s[n2+1] = temp

print("".join(s))
