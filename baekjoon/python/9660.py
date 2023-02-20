# TODO
import sys

n = int(sys.stdin.readline())

result_list = [False] * (n+1)
result_list[1] = True
result_list[2] = False
result_list[3] = True
result_list[4] = True
result_list[5] = True

for i in range(6, n+1):
    result_list[i] = False if all([result_list[i-1], result_list[i-3], result_list[i-4]]) else True

if result_list[n]:
    print("SK")
else:
    print("CY")
