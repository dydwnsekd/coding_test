import sys

cases = int(sys.stdin.readline())
h, m, s = 0, 0, 0

for _ in range(cases):
    mm, ss = map(int, sys.stdin.readline().split(":"))
    m += mm
    s += ss

m += s // 60
s = s % 60
h += m // 60
m = m % 60

print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")
