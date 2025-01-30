import sys

a_score = 0
b_score = 0

n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())

    if a > b:
        a_score += 1
    elif a < b:
        b_score += 1

print(a_score, b_score)
