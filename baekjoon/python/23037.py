import sys

result = 0
n = sys.stdin.readline().strip()

for i in n:
    result += pow(int(i), 5)

print(result)
