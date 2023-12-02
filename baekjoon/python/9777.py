import sys

result = {}
for i in range(1, 13):
    result[i] = 0

cases = int(sys.stdin.readline())

for _ in range(cases):
    id, birthday = sys.stdin.readline().split()
    month = int(birthday.split("/")[1])

    result[month] += 1

sorted_dict = sorted(result.items())

for i in sorted_dict:
    print(i[0], i[1])
