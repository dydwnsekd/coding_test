import sys

result = 0
n = int(sys.stdin.readline())

for _ in range(n):
    result += len(sys.stdin.readline().strip())

print(result)
