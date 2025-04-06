import sys, math

d, h, w = map(int, sys.stdin.readline().strip().split())

real_h = int(d * h // math.sqrt(w ** 2 + h ** 2))
real_w = int(d * w // math.sqrt(w ** 2 + h ** 2))

print(real_h, real_w)

