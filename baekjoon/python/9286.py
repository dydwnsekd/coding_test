import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    m = int(sys.stdin.readline())

    print("Case {}:".format(i))

    for _ in range(m):
        t = int(sys.stdin.readline())
        if t != 6:
            print(t+1)

