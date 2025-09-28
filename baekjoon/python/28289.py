import sys

p = int(sys.stdin.readline())
class_list = [0, 0, 0, 0]

for _ in range(p):
    g, c, n = map(int, sys.stdin.readline().split())

    if g in [2, 3]:
        if c in [1, 2]:
            class_list[0] += 1
        elif c == 3:
            class_list[1] += 1
        elif c == 4:
            class_list[2] += 1
    else:
        class_list[3] += 1

print("\n".join(map(str, class_list)))
