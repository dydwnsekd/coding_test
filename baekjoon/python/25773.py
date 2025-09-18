import sys

n = sys.stdin.readline().strip()
split_n = []

for i in n:
    split_n.append(i)

split_n = sorted(split_n, reverse=True)
print("".join(split_n))

