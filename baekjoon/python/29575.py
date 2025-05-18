import sys

win_dict = {}


n = int(sys.stdin.readline())

for _ in range(n):
    res, value = map(int, sys.stdin.readline().split())
    win_dict[res] = value

m = int(sys.stdin.readline())

money = m * -10

for _ in range(m):
    result = int(sys.stdin.readline())
    if result not in win_dict:
        money += win_dict[result]

print(money)

