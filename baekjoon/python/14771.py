# import sys
#
# k = int(sys.stdin.readline())
#
# for i in range(k):
#     result = 0
#     ad_list = []
#     ad_info = []
#
#     n, v = map(int, sys.stdin.readline().split())
#
#     for _ in range(n):
#         ad_list.append(list(map(int, sys.stdin.readline().split())))
#
#     for _ in range(v):
#         ad_info.append(list(map(int, sys.stdin.readline().split())))
#
#     for j in ad_info:
#         if ad_list[j[0] - 1][0] == 1:
#             result += ad_list[j[0]-1][1]
#         if ad_list[j[1] - 1][0] == 1:
#             result += ad_list[j[1]-1][1]
#
#         if j[2] == 1 and ad_list[j[0]-1][0] == 0:
#             result += ad_list[j[0]-1][1]
#         elif j[2] == 2 and ad_list[j[1]-1][0] == 0:
#             result += ad_list[j[1]-1][1]
#
#     print(f"Data Set {i+1}:")
#     print(result)
#     print()
#
#

import sys

k = int(sys.stdin.readline())

for i in range(1, k + 1):
    result = 0

    n, v = map(int, sys.stdin.readline().split())

    ad_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ad_info = [list(map(int, sys.stdin.readline().split())) for _ in range(v)]

    for j0, j1, flag in ad_info:
        left_ad = ad_list[j0 - 1]
        right_ad = ad_list[j1 - 1]

        if left_ad[0] == 1:
            result += left_ad[1]
        if right_ad[0] == 1:
            result += right_ad[1]

        if flag == 1 and left_ad[0] == 0:
            result += left_ad[1]
        elif flag == 2 and right_ad[0] == 0:
            result += right_ad[1]

    print(f"Data Set {i}:\n{result}\n")