import sys

result = 0

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().strip()

    if "01" in s or "OI" in s:
        result += 1

print(result)
