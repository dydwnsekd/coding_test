import sys, math

t = int(sys.stdin.readline())

for _ in range(t):

    a, b = map(int, sys.stdin.readline().strip().split())
    a_area = a * a * round(math.sqrt(3), 2) / 4
    b_area = b * b * round(math.sqrt(3), 2) / 4

    print(math.ceil(a_area / b_area))

