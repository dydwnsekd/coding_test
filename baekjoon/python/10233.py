import sys

while True:
    x, y, s = list(map(int, sys.stdin.readline().split()))
    max_value = -1
    if x == 0 and y == 0 and s == 0:
        break
    else:
        p = round((s * 100) / (100 + x))
        for i in range(1, p//2):
            j = p - i
            i_value = round(i * (100+y) / 100)
            j_value = round(j * (100+y) / 100)
            temp = i_value + j_value

            if temp > max_value:
                max_value = temp

        print(max_value)
