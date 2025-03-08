import sys

n, m = map(int, sys.stdin.readline().strip().split())
s_list = []
ss_list = []

for _ in range(n):
    s_list.append(sys.stdin.readline().strip())

for _ in range(n):
    ss_list.append(sys.stdin.readline().strip())

flag = True

for i in range(n):
    result = ""

    for j in s_list[i]:
        result += f"{j}{j}"

    if result != ss_list[i]:
        flag = False

if flag:
    print("Eyfa")
else:
    print("Not Eyfa")

