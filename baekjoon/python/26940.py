import sys

cases = int(sys.stdin.readline())
chocolate_count = list(map(int, sys.stdin.readline().split()))
new_box = 0
current_count = chocolate_count[0]

for i in chocolate_count[1:]:
    if current_count < i:
        new_box += 1

    current_count = i

print(new_box)

