import sys

n, b, h, w = list(map(int, sys.stdin.readline().split()))
minimum_value = sys.maxsize

for _ in range(h):
    h_value = int(sys.stdin.readline())
    possible_w = list(map(int, sys.stdin.readline().split()))
    if max(possible_w) >= n:
        if h_value * n <= b and minimum_value > n * h_value:
            minimum_value = n * h_value

if minimum_value == sys.maxsize:
    print("stay home")
else:
    print(minimum_value)

