import sys
import math

while True:
    x, y, s = list(map(int, sys.stdin.readline().split()))
    max_value = -1
    if x == 0 and y == 0 and s == 0:
        break
    else:
        for i in range(1, s//2):
            j = s - i
            i_origin = math.floor(i*100/(100+x))
            j_origin = math.floor(j*100/(100+x))

            i_value = math.floor(i_origin * (100 + y) / 100)
            j_value = math.floor(j_origin * (100 + y) / 100)

            temp = i_value + j_value

            if temp > max_value:
                max_value = temp

        print(max_value)
