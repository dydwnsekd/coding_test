import sys

n = int(sys.stdin.readline())

result_list = [0] * 1001
result_list[0] = 0
result_list[1] = 1
result_list[2] = 2
result_list[3] = 1

for i in range(4, 1001):
    result_list[i] = min(result_list[i-1], result_list[i-3]) + 1

if result_list[n] % 2 == 0:
    print("SK")
else:
    print("CY")

