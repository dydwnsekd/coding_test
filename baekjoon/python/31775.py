import sys

s_list = []

for _ in range(3):
    s_list.append(sys.stdin.readline().strip()[0])

if all(s in ["l", "p", "k"] for s in s_list):
    print("GLOBAL")
else:
    print("PONIX")


