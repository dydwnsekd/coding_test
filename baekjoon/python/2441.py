import sys
n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(" ", end="")
    for k in range(i, 0, -1):
        print("*", end="")
    print()
