import sys

n = int(sys.stdin.readline())
unique_num = set()

for i in range(n):
    unique_num.add(int(sys.stdin.readline()))

if len(unique_num) < 5:
    print("YES")
else:
    print("NO")

