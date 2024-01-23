import sys

n = int(sys.stdin.readline())
gift_list = [0] * n

for i in range(1, n+1):
    gift_list[int(sys.stdin.readline()) - 1] = i

for i in gift_list:
    print(i)
