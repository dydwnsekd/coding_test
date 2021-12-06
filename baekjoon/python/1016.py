#https://www.acmicpc.net/problem/1016

import sys
import math

min, max = map(int, (sys.stdin.readline().split()))

squared = [True] * (max-min+1)
answer = max-min+1
sqrt_max = int(math.sqrt(max))+2
for i in range(2, sqrt_max):
    pow_num = i * i

    if min % pow_num == 0:
        remainder = 0
    else:
        remainder = pow_num - (min % pow_num)

    for j in range(min+remainder, max+1, pow_num):
        # print("{} : {} : {}".format(j, pow_num, remainder))
        if squared[j-min] == False:
            pass
        elif j % pow_num == 0:
            squared[j-min] = False
            answer -= 1

print(answer)