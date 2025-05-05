import sys

n = int(sys.stdin.readline())
max_value = 0
player = ""

for i in range(n):
    s, n, c = sys.stdin.readline().split()
    s = int(s)

    if s > max_value and c == "Russia":
        player = n
        max_value = s

print(player)
