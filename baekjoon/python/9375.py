import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    clothes_dict = {}

    for _ in range(m):
        name, type = sys.stdin.readline().split()

