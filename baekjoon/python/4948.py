import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    else:
        count = 0
        sosu_list = [True for i in range((n*2)+1)]
        sosu_list[0] = False
        sosu_list[1] = False

        for i in range(2, (n*2)+1):
            if sosu_list[i]:
                for j in range(i+i, (n*2)+1, i):
                    sosu_list[j] = False

        for i in range(n+1, (n*2)+1):
            if sosu_list[i]:
                count += 1

        print(count)
