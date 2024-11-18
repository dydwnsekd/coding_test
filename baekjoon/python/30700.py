import sys

korea = ["K", "O", "R", "E", "A"]
korea_index = 0
result = 0

input_s = sys.stdin.readline().strip()

for s in input_s:
    if s == korea[korea_index]:
        korea_index += 1
        result += 1
        if korea_index == len(korea) :
            korea_index = 0

print(result)
