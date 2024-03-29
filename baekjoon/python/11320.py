import sys, math

t = int(sys.stdin.readline())

for _ in range(t):

    a, b = map(int, sys.stdin.readline().strip().split())
    a_area = a * a
    b_area = b * b

    print(math.ceil(a_area / b_area))

