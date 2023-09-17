import sys, math

area = int(sys.stdin.readline())

r = math.sqrt(area / math.pi)
print(r * 2 * math.pi)
