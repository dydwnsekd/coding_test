import sys

n = int(sys.stdin.readline())

while True:
    str_n = str(n)
    if len(str_n) == str_n.count("4") + str_n.count("7"):
        print(n)
        break
    else:
        n -= 1

