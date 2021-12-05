#https://www.acmicpc.net/problem/1016

import sys

min, max = map(int, (sys.stdin.readline().split()))

squared = [True] * max

for i in range(2, max+1):
    pow_num = i * i
    count = 1

    while(True):
        temp = pow_num * count
        if(temp > max):
            break
        else:
            squared[i] = False
            count+=1
    
print(squared[min:max+1].count(True))
