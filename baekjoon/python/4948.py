import sys

num_list = []

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    else:
        num_list.append(n)

max_num = max(num_list)
sosu_list = [True for i in range((max_num*2)+1)]
sosu_list[0] = False
sosu_list[1] = False

for i in range(2, (max_num * 2) + 1):
    if sosu_list[i]:
        for j in range(i + i, (max_num * 2) + 1, i):
            sosu_list[j] = False

for n in num_list:
    count = 0

    for i in range(n+1, (n*2)+1):
        if sosu_list[i]:
            count += 1

    print(count)
