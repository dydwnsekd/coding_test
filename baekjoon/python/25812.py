import sys

choice_1 = 0
choice_2 = 0

n, r = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    t = int(sys.stdin.readline())
    if t < r:
        choice_1 += 1
    elif t > r:
        choice_2 += 1

if choice_1 > choice_2:
    print(1)
elif choice_1 < choice_2:
    print(2)
else:
    print(0)
