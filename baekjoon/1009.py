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

    for j in range(100):
        count += 1
        r = (a * a) % 10
        if (r == 1):
            break

    b = b % count

    result = ((a ** b) % 10)

    if result == 0:
        print (0)
    else:
        print (result)
