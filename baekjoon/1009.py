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
    a,b = map(int, input().rstrip().split())

    r = '1'
    print (r[-1])

    for j in range(b):
        r = str(int(r[-1]) * a)

    print (r[-1])
