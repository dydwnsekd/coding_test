import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

if s[:n//2] == s[n//2:]:
    print("YES")
else:
    print("NO")

