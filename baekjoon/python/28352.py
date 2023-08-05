import sys, math

n = int(sys.stdin.readline())
fac_num = 1
week_sec = 604800

for i in range(n, 1, -1):
    fac_num *= i

print(fac_num // week_sec)

