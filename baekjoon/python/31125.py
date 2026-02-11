import sys

t = int(sys.stdin.readline())

def sum_dice(n, f, m):
    result = []
    for i in range(n*1+m, n*f+m+1):
        result.append(i)

    return result

for i in range(t):
    b, n ,f, m = map(int, sys.stdin.readline().split())

    if b in sum_dice(n, m, f):
        print('YES')
    else:
        print('NO')

