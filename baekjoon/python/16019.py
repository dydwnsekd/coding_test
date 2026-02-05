import sys

# git commit test

d = list(map(int, sys.stdin.readline().strip().split()))

pos = [0] * 5
for i in range(1, 5):
    pos[i] = pos[i - 1] + d[i - 1]

for i in range(5):
    for j in range(5):
        if j > 0:
            print(' ', end='')
        print(abs(pos[i] - pos[j]), end='')
    print()
