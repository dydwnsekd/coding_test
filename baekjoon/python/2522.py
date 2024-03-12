import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print('%s%s' % (' ' * (n-i), '*' * i))

for i in range(1, n):
    print('%s%s' % (' ' * i, '*' * (n-i)))

