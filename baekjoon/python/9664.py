import sys
import math

n = int(sys.stdin.readline())
o = int(sys.stdin.readline())
result = []

estimated_value = math.ceil(o * (n / (n-1)))

if estimated_value-1-o <= estimated_value // n:
    result.append(estimated_value-1)
if estimated_value-o <= estimated_value // n:
    result.append(estimated_value)
else:
    result.append(estimated_value-1)

print(f"{result[0]} {result[1]}")
