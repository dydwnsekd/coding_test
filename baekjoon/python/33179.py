import sys
import math

result = 0

n = int(sys.stdin.readline())
pages = list(map(int, sys.stdin.readline().split()))

for page in pages:
    result += math.ceil(page / 2)

print(result)

