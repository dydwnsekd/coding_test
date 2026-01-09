import sys

scores = list(map(int, sys.stdin.readline().strip().split()))
n = int(sys.stdin.readline().strip())

total = 0

for _ in range(n):
    b, l, s = sys.stdin.readline().strip().split()
    b = int(b)
    l = float(l)
    s = int(s)

    if l < 2.0 or s < 17:
        continue

    total += scores[b]

print(total)
