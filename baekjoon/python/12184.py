"""
import sys

t = int(sys.stdin.readline())
for i in range(t):
    result = []

    n = int(sys.stdin.readline())

    bus_temp = list(map(int, (sys.stdin.readline().strip().split())))
    bus_list = []
    for j in range(n):
        bus_list.append([bus_temp[j*2], bus_temp[j*2+1]])

    p = int(sys.stdin.readline())
    for _ in range(p):
        bus_line = int(sys.stdin.readline())
        temp = 0
        for b in bus_list:
            if b[0] <= bus_line <= b[1]:
                temp += 1

        result.append(str(temp))

    print(f"Case #{i+1}: {' '.join(result)}")

    t = sys.stdin.readline()
"""

import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n = int(sys.stdin.readline())
    bus_temp = list(map(int, sys.stdin.readline().split()))
    bus_list = [(bus_temp[i], bus_temp[i + 1]) for i in range(0, 2 * n, 2)]

    p = int(sys.stdin.readline().strip())
    result = []

    for _ in range(p):
        bus_line = int(sys.stdin.readline().strip())
        count = 0

        for start, end in bus_list:
            if start <= bus_line <= end:
                count += 1

        result.append(str(count))

    print(f"Case #{case}: {' '.join(result)}")

    sys.stdin.readline()
