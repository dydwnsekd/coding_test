import sys
import re

car_pattern = re.compile(sys.stdin.readline().strip().replace("*", "."))
cases = int(sys.stdin.readline())
result = 0
result_list = []

for _ in range(cases):
    t = sys.stdin.readline().strip()
    if car_pattern.match(t):
        result += 1
        result_list.append(t)


print(result)
for c in result_list:
    print(c)

