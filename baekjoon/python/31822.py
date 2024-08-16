import sys

result = 0

code = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

for _ in range(n):
    if code[:5] == sys.stdin.readline().strip()[:5]:
        result += 1

print(result)
