import sys

result = 0

n = int(sys.stdin.readline())
storkes = list(map(int, sys.stdin.readline().split()))

for i in range(len(storkes)):
    if storkes[i] > 7:
        storkes[i] = 7

    if i % 2 == 0:
        result += storkes[i] - 2
    else:
        result += storkes[i] - 3

print(result)

