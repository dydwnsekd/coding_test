import sys

alpha_dict = {}

for i in range(1, 27):
    alpha_dict[chr(i+64)] = i

while True:
    str = sys.stdin.readline().strip()
    sum = 0
    if str == "#":
        break
    else:
        for i in range(1, len(str)+1):
            sum += i * alpha_dict[str[i-1]]
        print(sum)
