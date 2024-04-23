import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().strip()

    if s[-1] != '0' and s.count('0') == 1:
        s = s[:s.index('0')] + '1'
    elif s.count('1') == 1:
        s = s[:s.index('1')+1]

    if s[-1] == "1" and len(s) % 2 == 0:
        print(0)
    elif s[-1] == "1" and len(s) % 2 == 1:
        print(1)
    elif s[-1] == "0" and len(s) % 2 == 0:
        print(1)
    elif s[-1] == "0" and len(s) % 2 == 1:
        print(0)

