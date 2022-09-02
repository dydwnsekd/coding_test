import sys

count = 0
x, y = list(sys.stdin.readline().split())

if len(x) == len(y):
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
    min_value = count

else:
    min_value = 999
    for i in range(len(y)-len(x)+1):
        count = 0
        for j in range(len(x)):
            if y[i+j] != x[j]:
                count += 1

        min_value = min([min_value, count])

print(min_value)

