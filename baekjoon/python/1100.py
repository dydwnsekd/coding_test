import sys

count = 0

for i in range(0,8):
    x = sys.stdin.readline()
    if i % 2 == 0:
        for j in range(0,8,2):
            if x[j] == "F":
                count += 1
    else:
        for j in range(1,8,2):
            if x[j] == "F":
                count += 1

print(count)