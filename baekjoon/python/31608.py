import sys

result = 0

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

for i in range(n):
    if s[i] != t[i]:
        result += 1

print(result)
