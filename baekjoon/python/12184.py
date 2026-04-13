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
