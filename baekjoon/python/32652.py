import sys

s = "AKARAKA"
add_s = "RAKA"

n = int(sys.stdin.readline())

if n == 1:
    print(s)
else:
    s += add_s * (n - 1)
    print(s)
