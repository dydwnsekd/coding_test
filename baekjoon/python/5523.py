import sys

a_score = 0
b_score = 0

n = int(sys.stdin.readline().strip())

for i in range(n):
    a, b  = map(int, sys.stdin.readline().strip().split())

    if a > b:
        a_score += 1
    elif a < b:
        b_score += 1

print(a_score, b_score)
