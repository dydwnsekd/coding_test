import sys

num = sys.stdin.readline().strip()
num_len = len(num)

print(f"{num[:num_len//2]} {num[num_len//2:]}")
