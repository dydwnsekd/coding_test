import sys

value = 0
weight = 0
cases = int(sys.stdin.readline())

for i in range(cases):
    box_info = sys.stdin.readline().split()

    if box_info[0] == "A":
        weight += 1000
        x = int(box_info[1]) // 12
        y = int(box_info[2]) // 12
        z = int(box_info[3]) // 12
        apple_count = x * y * z

        weight += apple_count * 500
        value += apple_count * 4000

    elif box_info[0] == "B":
        weight += 6000

print(weight)
print(value)
