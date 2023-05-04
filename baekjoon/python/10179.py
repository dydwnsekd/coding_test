import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    value = float(sys.stdin.readline())
    print("${:.2f}".format(round(value*0.8, 2)))
