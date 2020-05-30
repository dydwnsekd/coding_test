#https://www.acmicpc.net/problem/1009

import sys

n = int(sys.stdin.readline())
'''
for i in range(n):
    a,b = map(int, input().rstrip().split())
    b = b % 10
    print (a**b % 10)
'''


for i in range(n):
    r = 1
    count = 2
    
    a,b = map(int, input().rstrip().split())

    for j in range(b):
        count += 1
        r = (r * a) % 10
        if (r==a):
            b = b % count
            print ((r**b) % 10)
            break
        elif (r==0):
            print (0)
            break