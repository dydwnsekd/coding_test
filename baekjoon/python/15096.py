import sys

hits = 0

n = int(sys.stdin.readline())
hit_list = list(map(int, sys.stdin.readline().split()))

for i in hit_list:
    if i == -1:
        n -= 1
    else:
        hits += i

print(hits / n)
