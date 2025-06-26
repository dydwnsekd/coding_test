import sys

p = int(sys.stdin.readline())

cent_count = []
cent_value = [25, 10, 5, 1]

for i in range(4):
    cent_count.append(p // cent_value[i])
    p %= cent_value[i]

print(*cent_count)
