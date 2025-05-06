import sys

k = int(sys.stdin.readline())

for i in range(k):
    result = 0
    ad_list = []

    n, v = map(int, sys.stdin.readline().split())

    for _ in range(n):
        ad_list.append(list(map(int, sys.stdin.readline().split())))

    for _ in range(v):
        ad_info = list(map(int, sys.stdin.readline().split()))
        ad_view = ad_info[:2]
        click_index = ad_info[-1]

        for j in ad_view:
            if ad_list[j-1][0] == 1:
                result += ad_list[j-1][1]

        if ad_list[ad_view[click_index-1]][0] == 0:
            result += ad_list[ad_view[click_index-1]][1]

    print(result)


