import sys

end_num = int(10000 ** 0.5)

sosu_list = [True for i in range(10001)]
sosu_list[0] = False
sosu_list[1] = False

for i in range(2, end_num+1):
    if sosu_list[i]:
        for j in range(i+i, 10001, i):
            sosu_list[j] = False

min_value = int(sys.stdin.readline())
max_value = int(sys.stdin.readline())

sum_value = 0
min_sosu = 0

for i in range(min_value, max_value+1):
    if sosu_list[i]:
        sum_value += i
        if min_sosu == 0:
            min_sosu = i

if sum_value == 0:
    print(-1)
else:
    print(sum_value)
    print(min_sosu)
