import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    s = sys.stdin.readline().strip()
    print(s[0]+s[-1])
