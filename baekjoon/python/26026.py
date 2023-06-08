import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
cup_of_hand = 0
count = 0

for i in s:
    if i == "1":
        count += 1
        cup_of_hand = 2
    else:
        if cup_of_hand > 0:
            cup_of_hand -= 1
            count += 1

print(count)
