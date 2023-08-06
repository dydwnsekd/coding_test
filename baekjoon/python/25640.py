import sys

result = 0

jinho = sys.stdin.readline().strip()

n = int(sys.stdin.readline())
for _ in range(n):
    if sys.stdin.readline().strip() == jinho:
        result += 1

print(result)
