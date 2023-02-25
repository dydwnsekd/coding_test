import sys

count = 0

while True:
    n = int(sys.stdin.readline())
    temp = 1
    if n == -1:
        break

    for i in range(n+1):
        temp *= i

    if str(temp).count("0") % 2 == 0:
        count += 1

    print(count)
