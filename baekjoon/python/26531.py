import sys

s = sys.stdin.readline().strip()

a = int(s[0])
b = int(s[4])
c = int(s[8])

if a + b == c:
    print("YES")
else:
    print("NO")
