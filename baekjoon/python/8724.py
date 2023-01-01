import sys

n = int(sys.stdin.readline())
plankboard_list = list(map(int, sys.stdin.readline().split()))

result = 0
temp = 0

for i in plankboard_list:
    if i == 1:
        temp += 1
    else:
        if result < temp:
            result = temp
            temp = 0

if result < temp:
    print(temp)
else:
    print(result)
