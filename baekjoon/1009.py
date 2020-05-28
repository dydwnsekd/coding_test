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
    a,b = map(str, input().rstrip().split())

    for j in range(b):
        temp = int(a[0]) * int(a[0])
    
    print(a[0])
