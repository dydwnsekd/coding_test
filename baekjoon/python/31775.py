import sys

s_list = []
find_string = ["l", "k", "p"]

for _ in range(3):
    temp = sys.stdin.readline().strip()[0]

    if temp in find_string and temp not in s_list:
        s_list.append(temp)

if len(s_list) == 3:
    print("GLOBAL")
else:
    print("PONIX")

