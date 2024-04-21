import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().strip()

    if s[-1] != '0' and s.count('0') == 1:
        s = s[:s.index('0')] + '1'
    elif s.count('1') == 1:
        s = s[:s.index('1')+1]

    if len(s) % 2 == 0:
        print(0)
    else:
        print(1)
