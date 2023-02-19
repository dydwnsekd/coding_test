import sys

n = int(sys.stdin.readline())

result_list = [0] * 1001
result_list[0] = False
result_list[1] = False
result_list[2] = True
result_list[3] = False
result_list[4] = False
result_list[5] = True

for i in range(6, 1001):
    result_list[i] = False if any([result_list[i-1], result_list[i-3], result_list[i-4]]) else True

if result_list[n]:
    print("CY")
else:
    print("SK")

