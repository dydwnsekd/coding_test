import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

if len(set(num_list)) < 5:
    print("YES")
else:
    print("NO")

