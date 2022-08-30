import sys

count = 0
x, y = list(sys.stdin.readline().split())

if len(x) == len(y):
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
    print(count)

elif len(x) > len(y):
    min_value = 999
    for i in range(len(x)-len(y)):
        count = 0
        for j in range(len(y)):
            if x[i+j] != y[i+j]:
                count += 1

        if min_value > count:
            min_value = count

elif len(y) < len(x):
    min_value = 999
    for i in range(len(y)-len(x)):
        count = 0
        for j in range(len(x)):
            if y[i+j] != x[i+j]:
                count += 1

        if min_value > count:
            min_value = count

print(count)

