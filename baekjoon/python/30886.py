import sys
import math

n = int(sys.stdin.readline())

print(round((((math.sqrt(n/math.pi)+1)*2)**2), 10))
