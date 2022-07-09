import sys

min_value, max_value = list(map(int, sys.stdin.readline().split()))

end_num = int(max_value ** 0.5)

sosu_list = [True for i in range(max_value+1)]
sosu_list[0] = False
sosu_list[1] = False

for i in range(2, end_num+1):
    if sosu_list[i]:
        for j in range(i+i, max_value+1, i):
            sosu_list[j] = False

for i in range(min_value, max_value+1):
    if sosu_list[i]:
        print(i)