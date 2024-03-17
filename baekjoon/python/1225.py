import sys

result = 0
a, b = sys.stdin.readline().strip().split()

for i in range(len(a)):
    for j in range(len(b)):
        result += int(a[i]) * int(b[j])

print(result)
