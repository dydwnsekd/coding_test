import sys

n = int(sys.stdin.readline())

for _ in range(n):
    N, D, A, B, F = list(map(float, sys.stdin.readline().split(" ")))
    result = (D / (A + B)) * F
    print("{} {:.6f}".format(int(N), result))
