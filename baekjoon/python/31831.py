import sys

n, m = map(int, sys.stdin.readline().strip().split())
a_list = list(map(int, sys.stdin.readline().strip().split()))

current_stress = 0
result = 0

for a in a_list:
    if current_stress + a <= 0:
        current_stress = 0
    elif current_stress + a >= m:
        result += 1
        current_stress += a
    else:
        current_stress += a

print(result)
