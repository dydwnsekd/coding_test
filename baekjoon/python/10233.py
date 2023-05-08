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
            i_origin = math.ceil(i*100/(100+x))
            j_origin = math.ceil(j*100/(100+x))

            while True:
                j_temp = math.floor(j_origin * (100 + x) / 100)

                if i + j_temp == s:
                    i_value = math.floor(i_origin * (100 + y) / 100)
                    j_value = math.floor(j_origin * (100 + y) / 100)

                    temp = i_value + j_value

                    if temp > max_value:
                        max_value = temp
                elif i + j_temp > s:
                    break

                j_origin += 1

        print(max_value)