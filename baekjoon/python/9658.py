import sys

n = int(sys.stdin.readline())

# False -> CY 승, True -> SK 승
result_list = [False] * 1001
result_list[1] = False
result_list[2] = True
result_list[3] = False
result_list[4] = True
result_list[5] = False

for i in range(6, 1001):
    result_list[i] = True if any([result_list[i-1], result_list[i-3], result_list[i-4]]) else False

if result_list[n]:
    print("SK")
else:
    print("CY")
