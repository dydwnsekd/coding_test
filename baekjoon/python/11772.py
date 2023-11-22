import sys

result = 0
cases = int(sys.stdin.readline())

for _ in range(cases):
    temp = sys.stdin.readline().split()

    result += int(temp[:-1]) ** int(temp[-1])

print(result)
