import sys
import math

N = int(sys.stdin.readline())
num = 0
hap = 0

temp = 1

for i in range(N, N*N, N):
    hap += (i + temp)
    temp += 1
print (hap)