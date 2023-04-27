import sys

cases = int(sys.stdin.readline())
golden = 1.61803399
golden_min = golden - golden*0.01
golden_max = golden + golden*0.01

for _ in range(cases):
    a, b = map(float, sys.stdin.readline().split())
    ratio = max(a, b) / min(a, b)

    if golden_min <= ratio <= golden_max:
        print("golden")
    else:
        print("not")
