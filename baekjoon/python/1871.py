import sys

n = int(sys.stdin.readline())

for _ in range(n):
    l, d = sys.stdin.readline().strip().split("-")
    l = l[::-1]

    l_score = 0
    d_score = int(d)

    for i in range(len(l)):
        l_score += (26 ** i) * abs(ord(l[i]) - ord("A"))

    if abs(d_score - l_score) <= 100:
        print("nice")
    else:
        print("not nice")

