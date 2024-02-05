import sys

n = int(sys.stdin.readline())

for _ in range(n):
    b, p = map(float, sys.stdin.readline().strip().split())

    min_abpm = 60 / (p / (b-1))
    bpm = (b/p) * 60
    max_abpm = 2*bpm - min_abpm

    print(f"{min_abpm:0.4f} {bpm:0.4f} {max_abpm:0.4f}")

