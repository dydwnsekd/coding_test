import sys

result = 0
won_50000 = 154
won_10000 = 148
won_5000 = 142
won_1000 = 136

n = int(sys.stdin.readline())

for _ in range(n):
    w, h = map(int, sys.stdin.readline().strip().split())
    if w == won_50000:
        result += 50000
    elif w == won_10000:
        result += 10000
    elif w == won_5000:
        result += 5000
    elif w == won_1000:
        result += 1000

print(result)

