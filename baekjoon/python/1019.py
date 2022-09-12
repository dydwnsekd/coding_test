# https://www.acmicpc.net/problem/1019
import sys

n = int(sys.stdin.readline())
result_str = ""
result_list = [0] * 10

for i in range(1, n+1):
    str_num = str(i)
    result_str += str_num

for i in range(10):
    print(result_str.count(str(i)), end=' ')
