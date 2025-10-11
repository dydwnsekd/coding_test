import sys

n = sys.stdin.readline().strip()

while len(n) > 1:
    num_list = list(map(int, n))
    n = str(sum(num_list))

print(n)

