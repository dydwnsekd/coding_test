import sys

score_list = []

while True:
    n, m = map(int, sys.stdin.readline().split())
    max_sum = 0

    if n == 0 and m == 0:
        break

    for _ in range(m):
        score_list.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        temp = 0
        for j in range(m):
            temp += score_list[j][i]
            if temp > max_sum:
                max_sum = temp

    print(max_sum)

