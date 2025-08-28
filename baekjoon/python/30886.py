import sys
import math

n = int(sys.stdin.readline())

r = math.sqrt(n / math.pi)
value = ((r + 1) * 2) ** 2
print(f"{value:.10f}")
