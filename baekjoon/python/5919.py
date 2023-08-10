import sys

result = 0

n = int(sys.stdin.readline())
bales = []

for _ in range(n):
    bales.append(int(sys.stdin.readline()))

avg = sum(bales) // n

for b in bales:
    if b < avg:
        result += (avg-b)

print(result)
