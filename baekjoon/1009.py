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
    count = 1
    
    a,b = map(int, input().rstrip().split())
    a = a % 10
    r = a

    while(True):
        count += 1
        r = (r * a) % 10
        if (r == a):
            break

    b = b % (count-1)

    result = ((a ** b) % 10)

    if a == 6:
        print (6)
    elif result == 0:
        print (10)
    else:
        print (result)
