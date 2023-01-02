#TODO
import sys

n = int(sys.stdin.readline())
ret = 0

for s in range(1, n+1):
    for k in range(s, n+1):
        for i in range(k, n+1):
            ret = (ret+s*k//i) % 2010

print(ret)
