#https://www.acmicpc.net/problem/1019
import sys

n = int(sys.stdin.readline())
result_list = [0] * 10

for i in range(1, n+1):
    str_num = str(i)
    for j in str_num:
        result_list[int(j)] += 1

for i in result_list:
    print (i, end=' ')