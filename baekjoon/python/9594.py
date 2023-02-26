import sys
import re

p = re.compile('0*$')

while True:
    n = int(sys.stdin.readline())
    count = 1
    temp = 1
    if n == -1:
        break

    for i in range(1, n+1):
        temp *= i

        if len(p.findall(str(temp))[0]) % 2 == 0:
            count += 1

    print(count)
