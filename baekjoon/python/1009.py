#https://www.acmicpc.net/problem/1009

import sys

n = int(sys.stdin.readline())

for i in range(n):
    a,b = map(int, input().rstrip().split())
    a = a % 10
    r = 1
    num_list = []

    while(True):
        r = (r * a) % 10
        if (r in num_list):
            break
        else:
            num_list.append(r)
    
    b -= 1
    b %= len(num_list)
    
    if (num_list[b] == 0):
        print (10)
    else:
        print(num_list[b])