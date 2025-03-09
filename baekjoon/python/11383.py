# import sys
#
# n, m = map(int, sys.stdin.readline().strip().split())
# s_list = []
# ss_list = []
#
# for _ in range(n):
#     s_list.append(sys.stdin.readline().strip())
#
# for _ in range(n):
#     ss_list.append(sys.stdin.readline().strip())
#
# flag = True
#
# for i in range(n):
#     result = ""
#
#     for j in s_list[i]:
#         result += f"{j}{j}"
#
#     if result != ss_list[i]:
#         flag = False
#
# if flag:
#     print("Eyfa")
# else:
#     print("Not Eyfa")
#

import sys

n, m = map(int, sys.stdin.readline().split())

s_list = [sys.stdin.readline().strip() for _ in range(n)]
ss_list = [sys.stdin.readline().strip() for _ in range(n)]

# 모든 행이 조건을 만족하는지 확인
if all("".join(ch * 2 for ch in s_list[i]) == ss_list[i] for i in range(n)):
    print("Eyfa")
else:
    print("Not Eyfa")
