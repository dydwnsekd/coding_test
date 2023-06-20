import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    n = int(sys.stdin.readline())

    while True:
        n += 1
        str_n = str(n)

        flag = True
        for s in str_n:
            if s == "0":
                flag = False

        if flag:
            print(n)
            break
