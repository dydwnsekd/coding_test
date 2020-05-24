#https://www.acmicpc.net/problem/1009

import sys

n = int(sys.stdin.readline())

for i in range(n):
    a,b = map(int, input().rstrip().split())
    
    print (a**b)
    print (a**b % 10)
