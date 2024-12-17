import sys

def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1

n = int(sys.stdin.readline())
for _ in range(n):
    case_num, m = map(int, sys.stdin.readline().strip().split())
    print(case_num, pisano_period(m))
