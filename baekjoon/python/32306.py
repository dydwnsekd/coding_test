import sys

one1, two1, three1 = map(int, sys.stdin.readline().strip().split())
one2, two2, three2 = map(int, sys.stdin.readline().strip().split())

score1 = one1 + 2 * two1 + 3 * three1
score2 = one2 + 2 * two2 + 3 * three2

if score1 > score2:
    print(1)
elif score1 < score2:
    print(2)
else:
    print(0)
