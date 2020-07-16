import sys
import math

count = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split(" ")))

num_list.sort()

if count % 2 == 1:
    print (num_list[math.floor(count/2)] ** 2)

else:
    print (num_list[0] * num_list[-1])