import sys

result = 0

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

for i in range(n):
    result += ord(s[i]) - ord(t[i])

print(result)
