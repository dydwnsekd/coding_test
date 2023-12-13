import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    d, n, s, p = list(map(int, sys.stdin.readline().split()))

    serialize_time = n * s
    parallelize_time = d + (n * p)

    if parallelize_time > serialize_time:
        print("do not parallelize")
    elif parallelize_time < serialize_time:
        print("parallelize")
    else:
        print("does not matter")

