import sys

h, m = list(map(int, sys.stdin.readline().split()))
m += int(sys.stdin.readline())

if m >= 60:
    h_t = m // 60
    m = m % 60

    h += h_t
    if h >= 24:
        h = h % 24

print(f"{h} {m}")
