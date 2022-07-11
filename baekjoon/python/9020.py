import sys

end_num = int(10000 ** 0.5)

sosu_list = [True for i in range(1001)]
sosu_list[0] = False
sosu_list[1] = False

for i in range(2, end_num+1):
    if sosu_list[i] == True:
        for j in range(i+i, 1001, i):
            sosu_list[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    temp = n//2
    while True:
        if sosu_list[temp]:
            print(f"{temp} {n-temp}")
            break
        else:
            temp -= 1
