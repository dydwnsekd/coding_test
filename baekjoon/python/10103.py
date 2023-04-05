import sys

cases = int(sys.stdin.readline())
p1_score = p2_score = 100

for _ in range(cases):
    s1, s2 = list(map(int, sys.stdin.readline().split()))

    if s1 > s2:
        p2_score -= s1
    elif s1 < s2:
        p1_score -= s2

print(p1_score)
print(p2_score)
