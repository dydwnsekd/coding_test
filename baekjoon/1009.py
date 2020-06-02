#https://www.acmicpc.net/problem/1009

import sys

n = int(sys.stdin.readline())

for i in range(n):
    count = 0
    
    a,b = map(int, input().rstrip().split())
    a = a % 10
    r = a

    while(True):
        count += 1
        r = (r * a) % 10
        if (r == a):
            break
    
    b = b % count

    result = ((a ** b) % 10)
    
    if (a==6 or a==5):
        print (a)
    elif result == 0:
        print (10)
    else:
        print (result)