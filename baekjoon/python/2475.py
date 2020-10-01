import sys

num_list = list(map(int, sys.stdin.readline().split(" ")))
result_num = 0

for i in num_list:
    result_num += i ** 2

print (result_num % 10)