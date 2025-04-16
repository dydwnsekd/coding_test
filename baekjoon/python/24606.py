import sys

result = 1

n1 = sys.stdin.readline().strip()
n2 = sys.stdin.readline().strip()

for i in range(4):
    if n1[i] != n2[i]:
        result *= 2

print(result)

