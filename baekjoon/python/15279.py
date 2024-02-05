import sys

n = int(sys.stdin.readline())

for _ in range(n):
    b, p = map(float, sys.stdin.readline().strip().split())

    min_abpm = round(60 / (p / (b-1)), 4)
    bpm = round((b/p) * 60, 4)
    max_abpm = round(min_abpm + bpm, 4)

    print(min_abpm, bpm, max_abpm)
