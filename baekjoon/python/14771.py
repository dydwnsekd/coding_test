import sys

k = int(sys.stdin.readline())

for i in range(k):
    result = 0
    ad_list = []
    ad_info = []

    n, v = map(int, sys.stdin.readline().split())

    for _ in range(n):
        ad_list.append(list(map(int, sys.stdin.readline().split())))

    for _ in range(v):
        ad_info.append(list(map(int, sys.stdin.readline().split())))

    for j in ad_info:
        if ad_list[j[0] - 1][0] == 1:
            result += ad_list[j[0]-1][1]
        if ad_list[j[1] - 1][0] == 1:
            result += ad_list[j[1]-1][1]

        if j[2] == 1 and ad_list[j[0]-1][0] == 0:
            result += ad_list[j[0]-1][1]
        elif j[2] == 2 and ad_list[j[1]-1][0] == 0:
            result += ad_list[j[1]-1][1]

    print(f"Data Set {i+1}:")
    print(result)


