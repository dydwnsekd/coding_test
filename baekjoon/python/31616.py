import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

c = s[0]

if s.count(c) == n:
    print("Yes")
else:
    print("No")
