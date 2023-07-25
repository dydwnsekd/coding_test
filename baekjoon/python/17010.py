import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    n, x = sys.stdin.readline().strip().split()
    # n, x = sys.stdin.readline().rstrip().split()
    print(x * int(n))
