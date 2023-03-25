# TODO
# https://yiyj1030.tistory.com/490
# https://degurii.tistory.com/158
import sys
import math

def count_one(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

start_num, end_num = map(int, sys.stdin.readline().split(" "))

count = 0

for i in range(start_num, end_num+1):
    count += count_one(i)

print(count)

